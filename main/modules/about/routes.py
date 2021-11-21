from flask import Blueprint, render_template


about = Blueprint("about", __name__, url_prefix="/about")


@about.route("/")
def index():
    return render_template("about/index.html")


@about.route("/mission-and-vision")
def mission_and_vision():
    return render_template("about/mission-and-vision.html")
