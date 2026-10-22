from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix='/auth')

@bp.route("/")
def index():
    return 'auth:index'


@bp.route("/login", methods=["POST", "GET"])
def login():
    return '<p>auth:login</p>'

@bp.route("/logout")
def logout():
    return '<p>auth:logout</p>'

@bp.route("/register", methods=["GET", "POST"])
def register():
    return "<p>auth:register</p>"