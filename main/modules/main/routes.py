from flask import Blueprint, render_template


main = Blueprint("main", __name__, url_prefix="")


# We may want to add a home page later.
# For now, just render the "about" page instead.
@main.route("/")
def index():
    return render_template("about/index.html")
