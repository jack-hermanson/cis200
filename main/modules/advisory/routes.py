from flask import Blueprint, render_template, redirect, url_for


advisory = Blueprint("advisory", __name__, url_prefix="/meet-the-teams")


@advisory.route("/")
def index():
    return render_template("meet-the-teams/index.html")


@advisory.route("/learning-support")
def learning_support():
    return redirect(url_for("advisory.learning_support_001"))


@advisory.route("/learning-support-001")
def learning_support_001():
    return render_template("meet-the-teams/learning-support-001.html")


@advisory.route("/learning-support-004")
def learning_support_004():
    return render_template("meet-the-teams/learning-support-004.html")


@advisory.route("/project-management")
def project_management():
    return render_template("meet-the-teams/project-management.html")

  
@advisory.route("/marketing")
def marketing():
    return render_template("meet-the-teams/marketing.html")


@advisory.route("/hr")
def hr():
    return render_template("meet-the-teams/hr.html")


@advisory.route("/multimedia")
def multimedia():
    return render_template("meet-the-teams/multimedia.html")


@advisory.route("/is-team")
def is_team():
    return render_template("meet-the-teams/is-team.html")
