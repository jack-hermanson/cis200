from flask import Blueprint, render_template


economic = Blueprint("economic", __name__, url_prefix="/economic")


@economic.route("/")
def index():
    return render_template("economic/index.html")


@economic.route("/wells-fargo-scandal")
def wells_fargo_scandal():
    return render_template("economic/wells-fargo-scandal.html")


@economic.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("economic/homelessness-in-colorado.html")


@economic.route("/affordable-housing")
def affordable_housing():
    return render_template("economic/affordable-housing.html")


@economic.route("/forensicact-moneylaundering")
def forensicact_moneylaundering():
    return render_template("economic/forensicact-moneylaundering.html")
