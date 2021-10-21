from flask import Blueprint, render_template

from main.utils.ApiRequest import ApiRequest

sandbox = Blueprint("sandbox", __name__, url_prefix="/sandbox")


@sandbox.route("/")
def index():
    return render_template("sandbox/index.html")


@sandbox.route("/cat-facts")
def cat_facts():
    cat_data = ApiRequest("https://catfact.ninja/fact").make_request()
    return render_template("sandbox/cat-facts.html",
                           cat_data=cat_data)


@sandbox.route("/expenditures")
def expenditures():
    return render_template("sandbox/expenditures.html")