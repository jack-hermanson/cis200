from flask import Blueprint, render_template


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return render_template("advisory/index.html")

@advisory.route("/learning-support")
def learning_support():
    return render_template("advisory/learning-support.html")
