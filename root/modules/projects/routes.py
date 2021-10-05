from flask import Blueprint, render_template


projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.route("/")
def index():
    return render_template("projects/index.html")
