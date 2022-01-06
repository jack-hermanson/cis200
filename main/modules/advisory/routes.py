from flask import Blueprint, render_template, redirect, url_for


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return render_template("advisory/index.html")


@advisory.route("/learning-support")
def learning_support():
    return redirect(url_for("advisory.learning_support_001"))


@advisory.route("/learning-support-001")
def learning_support_001():
    return render_template("advisory/learning-support-001.html")


@advisory.route("/learning-support-004")
def learning_support_004():
    return render_template("advisory/learning-support-004.html")


@advisory.route("/project-management")
def project_management():
    return render_template("advisory/project-management.html")

  
@advisory.route("/marketing")
def marketing():
    return render_template("advisory/marketing.html")


@advisory.route("/hr")
def hr():
    return render_template("advisory/hr.html")


@advisory.route("/multimedia")
def multimedia():
    return render_template("advisory/multimedia.html")
