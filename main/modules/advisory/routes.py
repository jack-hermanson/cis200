from flask import Blueprint, render_template


advisory = Blueprint("advisory", __name__, url_prefix="/advisory")


@advisory.route("/")
def index():
    return "advisory"