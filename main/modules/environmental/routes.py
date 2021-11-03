from flask import Blueprint, render_template


environmental = Blueprint("environmental", __name__, url_prefix="/environmental")


@environmental.route("/")
def index():
    return render_template("environmental/index.html")

@environmental.route("/sustainable-restaurants")
def sustainable_restaurants():
    return render_template("environmental/sustainable_restaurants.html")