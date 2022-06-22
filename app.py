from flask import Flask, render_template

import config
from exts import db

from blueprints import index_bp
from blueprints import user_bp
from blueprints import data_bp
from blueprints import search_bp

import click
from models import User, Magazine, Article

import xlrd
import os
import re

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(data_bp)
app.register_blueprint(search_bp)

file_path = 'D:\\Gu\\Desktop\\大软目录'


@app.cli.command()
def deletedb():
    article = Article.query.all()
    for i in article:
        db.session.delete(i)
    db.session.commit()

    magazine = Magazine.query.all()
    for i in magazine:
        db.session.delete(i)
    db.session.commit()

    click.echo('Delete database.')


@app.cli.command()  # 注册为命令
# @click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb():

    file_list = os.listdir(file_path)
    for file in file_list:
        matchObj = re.match(r'【(\d+)年(\d+)月(.*)】.xlsx', file)
        if matchObj is None:
            click.echo('None')
            continue
        year = matchObj.group(1)
        if not 1993 < int(year) < 2020:
            continue
        month = matchObj.group(2)
        week = matchObj.group(3)
        if int(month) <= 9:
            month = "0" + month
        if week != "":
            if week == "上":
                week = 1
            elif week == "中":
                week = 2
            elif week == "下":
                week = 3
        else:
            week = 0

        id_maga = year + month + str(week)
        magazine = Magazine(id=id_maga, collected=1)
        db.session.add(magazine)
        db.session.commit()

        xl_path = file_path + "\\" + file
        data = xlrd.open_workbook(xl_path)
        table = data.sheet_by_name('Sheet1')

        nrows = table.nrows
        a_index = 0
        for i in range(4, nrows):
            a_title = table.cell(i, 0).value
            if a_title == "":
                continue
            a_pageNum = table.cell(i, 1).value
            article = Article(id_magazine=id_maga, index=a_index, title=a_title, pageNum=a_pageNum)
            db.session.add(article)
            a_index += 1

    db.session.commit()
    click.echo('Initialized database.')  # 输出提示信息


@app.route("/jq")
def login():
    return render_template("JQtry.html")


if __name__ == '__main__':
    app.run()
