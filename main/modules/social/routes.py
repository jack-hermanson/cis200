from flask import Blueprint, render_template


social = Blueprint("social", __name__, url_prefix="/social")


@social.route("/")
def index():
    return render_template("social/index.html")

@social.route("/worksite-wellness")
def worksite_wellness():
    return render_template("social/worksite-wellness.html")

@social.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("social/homelessness-in-colorado.html")