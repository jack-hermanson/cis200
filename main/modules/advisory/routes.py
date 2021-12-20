from flask import Blueprint, render_template


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return render_template("advisory/index.html")


@advisory.route("/learning-support")
def learning_support_team():
    return render_template("advisory/learning-support.html")


@advisory.route("/learning-support-team")
def learning_support():
    return render_template("advisory/learning-support-team.html")


@advisory.route("/project-management")
def project_management():
    return render_template("advisory/project-management.html")

  
@advisory.route("/marketing")
def marketing():
    return render_template("advisory/marketing.html")


@advisory.route("/hr")
def hr():
    return render_template("advisory/hr.html")
