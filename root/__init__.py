from flask_bcrypt import Bcrypt
from flask import Flask
from flask_talisman import Talisman, DEFAULT_CSP_POLICY

from root.config import Config

bcrypt = Bcrypt()


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
                "cdn.jsdelivr.net"
            ],
            "script-src": [
                "'self'",
            ],
        },
        content_security_policy_nonce_in=["script-src"]
    )

    # set up bcrypt
    bcrypt.init_app(app)

    # register blueprints
    from root.modules.main.routes import main
    app.register_blueprint(main)

    from root.modules.projects.routes import projects
    app.register_blueprint(projects)

    # return the app
    return app

