from flask import Blueprint, render_template


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return render_template("advisory/index.html")


@advisory.route("/is-team")
def is_team():
    return render_template("advisory/is-team.html")


@advisory.route("/project-management")
def project_management():
    return render_template("advisory/project-management.html")

  
@advisory.route("/marketing")
def marketing():
    return render_template("advisory/marketing.html")


@advisory.route("/hr")
def hr():
    return render_template("advisory/hr.html")
