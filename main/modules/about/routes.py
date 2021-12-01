from flask import Blueprint, render_template


about = Blueprint("about", __name__, url_prefix="/about")


@about.route("/")
def index():
    return render_template("about/index.html")


@about.route("/mission-and-vision")
def mission_and_vision():
    return render_template("about/mission-and-vision.html")


@about.route("/projects")
def projects():
    return render_template("about/projects.html")

@about.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("about/homelessness-in-colorado.html")

@about.route("/social-isolation")
def social_isolation():
    return render_template("about/social-isolation.html")

@about.route("/sustainable-restaurants")
def restaurant_sustainability():
    return render_template("about/sustainable-restaurants.html")