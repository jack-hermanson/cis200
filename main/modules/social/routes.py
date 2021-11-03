from flask import Blueprint, render_template


social = Blueprint("social", __name__, url_prefix="/social")


@social.route("/")
def index():
    return render_template("social/index.html")

@social.route("/scamming")
def scamming():
    return render_template("social/scamming.html") 