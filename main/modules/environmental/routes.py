from flask import Blueprint, render_template


environmental = Blueprint("environmental", __name__, url_prefix="/environmental")


@environmental.route("/")
def index():
    return render_template("environmental/index.html")
