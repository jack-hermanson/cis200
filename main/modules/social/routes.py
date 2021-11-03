from flask import Blueprint, render_template


social = Blueprint("social", __name__, url_prefix="/social")


@social.route("/")
def index():
    return render_template("social/index.html")


@social.route("/health-foods")
def health_foods():
    return render_template("social/health-foods.html")
  

@social.route("/scamming")
def scamming():
    return render_template("social/scamming.html") 

  
@social.route("/worksite-wellness")
def worksite_wellness():
    return render_template("social/worksite-wellness.html")


@social.route("/wells-fargo-scandal")
def wells_fargo_scandal():
    return render_template("social/wells-fargo-scandal.html")


@social.route("/social-isolation")
def social_isolation():
    return render_template("social/social-isolation.html")
  

@social.route("/information-privacy")
def information_privacy():
    return render_template("social/information-privacy.html")
  

@social.route("/homelessness-in-colorado")
def homelessness_in_colorado():
    return render_template("social/homelessness-in-colorado.html")

