from flask import Blueprint
from exts import db
from models import User, Magazine, Article
import json

bp = Blueprint("data", __name__, url_prefix="/data")  # url_prefix 视图前缀

testInfo = {}
magaList = []


@bp.route('/test', methods=['GET', 'POST'])
def test_post():
    testInfo['name'] = 'xiaoming'
    testInfo['age'] = '28'
    return json.dumps(testInfo)


@bp.route('/show')
def show_date():
    print(Magazine.query.all())
    print(type(Magazine.query.all()[1]))
    return "测试"
