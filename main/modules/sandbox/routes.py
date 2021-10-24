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


@sandbox.route("/random-users")
def random_users():
    random_users_data = ApiRequest("https://randomuser.me/api/").make_request()
    return render_template("sandbox/random-users.html", random_user_data = random_users_data)
  

@sandbox.route("/bored")
def bored():
    bored_data = ApiRequest("https://www.boredapi.com/api/activity").make_request()
    return render_template("sandbox/bored.html",
        bored_data=bored_data)


@sandbox.route("/universities")
def universities():
    universities_data = ApiRequest("http://universities.hipolabs.com/search?country=United+States").make_request()
    return render_template("sandbox/universities.html",
        universities_data=universities_data)
