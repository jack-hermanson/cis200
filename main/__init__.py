# from flask_bcrypt import Bcrypt
from flask import Flask
from flask_mail import Mail
from flask_talisman import Talisman

from main.config import Config

# bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):

    # set up file paths for static resources
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="web/static",
        template_folder="web/templates"
    )

    # set up environment variables
    app.config.from_object(config_class)

    # set up https / security
    Talisman(
        app,
        content_security_policy={
            "default-src": [
                "'self'",
                "cdn.jsdelivr.net",
                "www.opensecrets.org/",
                "https://fonts.googleapis.com",
            ],
            "font-src": [
                "cdn.jsdelivr.net",
                "https://fonts.gstatic.com"
            ],
            "script-src": [
                "'self'",
            ],
            "img-src data:": [
                "unsafe-eval",
                "https://images.unsplash.com/",
                "https://images.dog.ceo",
                "https://imgs.xkcd.com/",
                "https://cdn2.thecatapi.com",
                "https://i.imgur.com/ZhPqSpV.png",
                "'self'"
            ],
            "frame-src": [
                "https://www.youtube.com/"
            ]
        },
        content_security_policy_nonce_in=["script-src"]
    )

    # set up bcrypt
    # bcrypt.init_app(app)
    # set up mail
    mail.init_app(app)

    # register blueprints/routes
    from .modules.main.routes import main
    from .modules.contact.routes import contact
    from .modules.economic.routes import economic
    from .modules.environmental.routes import environmental
    from .modules.main.routes import main
    from .modules.sandbox.routes import sandbox
    from .modules.social.routes import social
    from .modules.advisory.routes import advisory

    for blueprint in [main, contact, economic, environmental, main, sandbox, social, advisory]:
        app.register_blueprint(blueprint)

    # return the app
    return app

