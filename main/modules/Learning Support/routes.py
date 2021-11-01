from flask import Blueprint, render_template


learningsupport = Blueprint("learningsupport", __name__, url_prefix="/learningsupport")


@learningsupport.route("/")
def index():
    return render_template("learningsupport/index.html")
