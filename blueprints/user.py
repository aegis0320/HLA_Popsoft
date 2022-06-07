from flask import Blueprint

bp = Blueprint("user", __name__, url_prefix="/user")  # url_prefix 视图前缀


@bp.route("/login")
def login():
    return "登录"
