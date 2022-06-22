from flask import Blueprint, render_template, request, redirect
from models import User, Magazine, Article


from exts import db

bp = Blueprint("search", __name__, url_prefix="/search")  # url_prefix 视图前缀


@bp.route("/", methods=['GET', 'POST'])
def search():
    result_list = []
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        key = request.form.get('key')  # 传入表单对应输入字段的 name 值
        return redirect("/search/" + key)
    return render_template("search_by.html", result_list=result_list)


@bp.route('/<key_word>', methods=['GET', 'POST'])
def search_by(key_word):
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        key = request.form.get('key')  # 传入表单对应输入字段的 name 值
        return redirect("/search/"+key)

    result_list = []
    ress = db.session.query(Article).filter(Article.title.like('%{}%'.format(key_word))).all()

    for res in ress:
        id_maga = str(res.id_magazine)
        year = id_maga[0:4]
        month = str(int(id_maga[4:6]))
        if id_maga[6] == "1":
            week = "上"
        elif id_maga[6] == "2":
            week = "中"
        elif id_maga[6] == "3":
            week = "下"
        else:
            week = ""
        magaz = year + "年" + month + "月" + week
        result_list.append([res.title, magaz, res.pageNum])
    if not result_list:
        result_list.append(["无结果", "", ""])
    return render_template("search_by.html", result_list=result_list)
