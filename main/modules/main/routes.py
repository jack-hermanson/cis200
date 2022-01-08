from flask import Blueprint, render_template


main = Blueprint("main", __name__, url_prefix="")


# We may want to add a home page later.
# For now, just render the "about" page instead.
@main.route("/")
def index():
    return render_template("main/index.html")


@main.route("/mission-and-vision")
def mission_and_vision():
    return render_template("main/mission-and-vision.html")


@main.route("/featured-projects")
def projects():
    return render_template("main/projects.html")
