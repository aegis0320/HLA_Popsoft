from flask import Blueprint, render_template
from models import User, Magazine, Article
import json

bp = Blueprint("index", __name__, url_prefix="/")  # url_prefix 视图前缀
testList = [1, 2, 3]


@bp.route("/")
def login():
    print(make_list())
    return render_template("index.html", ma_dict=make_list())


@bp.route('/cata/<int:cata_id>', methods=['GET', 'POST'])
def make_catalogue(cata_id):
    tit_list = []
    at_list = Article.query.filter(Article.id_magazine == cata_id).order_by(Article.index).all()
    for at in at_list:
        tit_list.append([at.id_magazine, str(at.pageNum)])
    return json.dumps(tit_list)


def make_list():
    ma_list = []
    ma_dict = {}
    for ma in Magazine.query.all():
        ma_list.append(str(ma.id))
    for ma in ma_list:
        if ma[0: 4] not in ma_dict:
            ma_dict[ma[0: 4]] = {}
        if ma[4: 6] not in ma_dict[ma[0: 4]]:
            ma_dict[ma[0: 4]][ma[4: 6]] = []

        ma_dict[ma[0: 4]][ma[4: 6]].append(ma[6: 8])

    return ma_dict
