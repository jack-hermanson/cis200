from flask import Blueprint, render_template


projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.route("/wells-fargo-scandal")
def wells_fargo_scandal():
    return render_template("projects/wells-fargo-scandal.html")


@projects.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("projects/homelessness-in-colorado.html")


@projects.route("/affordable-housing")
def affordable_housing():
    return render_template("projects/affordable-housing.html")


@projects.route("/forensicact-moneylaundering")
def forensicact_moneylaundering():
    return render_template("projects/forensicact-moneylaundering.html")


@projects.route("/ecosurf")
def ecosurf():
    return render_template("projects/ecosurf.html")
