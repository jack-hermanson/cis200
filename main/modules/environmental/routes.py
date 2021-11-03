from flask import Blueprint, render_template


environmental = Blueprint("environmental", __name__, url_prefix="/environmental")


@environmental.route("/")
def index():
    return render_template("environmental/index.html")


@environmental.route("/agriculture-and-water")
def agriculture_and_water():
    return render_template("environmental/agriculture-and-water.html")