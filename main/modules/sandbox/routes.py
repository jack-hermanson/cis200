from flask import Blueprint, render_template


sandbox = Blueprint("sandbox", __name__, url_prefix="/sandbox")


@sandbox.route("/")
def index():
    return render_template("sandbox/index.html")


@sandbox.route("/expenditures")
def expenditures():
    return render_template("sandbox/expenditures.html")
