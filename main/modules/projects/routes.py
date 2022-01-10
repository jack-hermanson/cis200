from flask import Blueprint, render_template, redirect, url_for

projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.route("/")
def index():
    return redirect(url_for("main.projects"))


@projects.route("/wells-fargo-scandal")
def wells_fargo_scandal():
    return render_template("projects/wells-fargo-scandal.html")


@projects.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("projects/homelessness-in-colorado.html")


@projects.route("/affordable-housing")
def affordable_housing():
    return render_template("projects/affordable-housing.html")


@projects.route("/identity-theft-money-laundering")
def identity_theft_money_laundering():
    return render_template("projects/identity-theft-money-laundering.html")


@projects.route("/ecosurf")
def ecosurf():
    return render_template("projects/ecosurf.html")


@projects.route("/livestock-sustainability")
def livestock_sustainability():
    return render_template("projects/livestock-sustainability.html")


@projects.route("/sustainable-restaurants")
def sustainable_restaurants():
    return render_template("projects/sustainable-restaurants.html")


@projects.route("/csu-sustainability")
def csu_sustainability():
    return render_template("projects/csu-sustainability.html")


@projects.route("/food-production")
def food_production():
    return render_template("projects/food-production.html")


@projects.route("/health-foods")
def health_foods():
    return render_template("projects/health-foods.html")


@projects.route("/online-scamming")
def online_scamming():
    return render_template("projects/online-scamming.html")


@projects.route("/worksite-wellness")
def worksite_wellness():
    return render_template("projects/worksite-wellness.html")


@projects.route("/social-isolation")
def social_isolation():
    return render_template("projects/social-isolation.html")


@projects.route("/information-privacy")
def information_privacy():
    return render_template("projects/information-privacy.html")


@projects.route("/bias-in-the-news")
def bias_in_the_news():
    return render_template("projects/bias-in-the-news.html")


@projects.route("/normalizing-health")
def normalizing_health():
    return render_template("projects/normalizing-health.html")


@projects.route("/cookies")
def cookies():
    return render_template("projects/cookies.html")
