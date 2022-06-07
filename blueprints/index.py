from flask import Blueprint, render_template
from models import User, Magazine, Article

bp = Blueprint("index", __name__, url_prefix="/")  # url_prefix 视图前缀


@bp.route("/")
def login():
    print(make_list())
    return render_template("index.html", ma_dict=make_list())


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
