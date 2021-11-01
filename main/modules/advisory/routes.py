from flask import Blueprint, render_template


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return render_template("advisory/index.html")


@advisory.route("/project-management")
def project_management():
    return render_template("advisory/project-management.html")
