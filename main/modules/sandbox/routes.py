from flask import Blueprint, render_template

from main.utils.ApiRequest import ApiRequest

sandbox = Blueprint("sandbox", __name__, url_prefix="/sandbox")


@sandbox.route("/")
def index():
    return render_template("sandbox/index.html")


@sandbox.route("/cat-facts")
def cat_facts():
    cat_data = ApiRequest("https://catfact.ninja/fact").make_request()
    return render_template(
        "sandbox/cat-facts.html",
        cat_data=cat_data
    )


@sandbox.route("/expenditures")
def expenditures():
    return render_template("sandbox/expenditures.html")


@sandbox.route("/random-users")
def random_users():
    random_users_data = ApiRequest("https://randomuser.me/api/").make_request()
    return render_template(
        "sandbox/random-users.html",
        random_user_data=random_users_data
    )


@sandbox.route("/bored")
def bored():
    bored_data = ApiRequest("https://www.boredapi.com/api/activity").make_request()
    return render_template(
        "sandbox/bored.html",
        bored_data=bored_data
    )


@sandbox.route("/universities")
def universities():
    universities_data = ApiRequest("http://universities.hipolabs.com/search?country=United+States").make_request()
    for university in universities_data:
        name = university["name"]
        country = university["country"]
        domain = university["domains"][0]
    return render_template(
        "sandbox/universities.html",
        universities_data=universities_data
    )


@sandbox.route("/jokes")
def jokes():
    jokes_data = ApiRequest("https://v2.jokeapi.dev/joke/Any?type=twopart&blacklistFlags=nsfw,religious,racist,sexist,explicit").make_request()
    return render_template(
        "sandbox/jokes.html",
        jokes_data=jokes_data
    )


@sandbox.route("/dogs")
def dogs():
    dog1 = ApiRequest("https://dog.ceo/api/breed/retriever/images/random").make_request()
    dog2 = ApiRequest("https://dog.ceo/api/breed/retriever/images/random").make_request()
    return render_template(
        "sandbox/dogs.html",
        dogs_data=[dog1, dog2]
    )


@sandbox.route("/xkcd")
def xkcd():
    xkcd_data = ApiRequest("https://xkcd.com/info.0.json").make_request()
    return render_template(
        "sandbox/xkcd.html",
        xkcd_data=xkcd_data
    )


@sandbox.route("/tv-shows")
def tv_shows():
    tv_shows_data = ApiRequest("https://api.tvmaze.com/search/shows?q=golden%20girls").make_request()
    return render_template(
        "sandbox/tv-shows.html",
        tv_shows_data=tv_shows_data
    )


@sandbox.route("/facts")
def facts():
    facts_data = ApiRequest("https://uselessfacts.jsph.pl/random.json?language=en").make_request()
    return render_template(
        "sandbox/facts.html",
        facts_data=facts_data
    )

  
@sandbox.route("/kitten")
def kitten():
    kitten_data = ApiRequest("https://api.thecatapi.com/v1/images/search").make_request()
    return render_template(
        "sandbox/kitten.html", 
        kitten_data = kitten_data
    )

  
@sandbox.route("/anime")
def anime():
    anime_data = ApiRequest("https://api.jikan.moe/v3/search/anime?q=naruto").make_request()
    return render_template(
        "sandbox/anime.html",
        anime_data=anime_data
    )


@sandbox.route("/IP")
def IP():
    ip_data = ApiRequest("https://api.ipify.org/?format=json").make_request()
    return render_template("sandbox/IP.html",
        ip_data=ip_data)
