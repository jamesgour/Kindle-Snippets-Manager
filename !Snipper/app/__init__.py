from flask import Flask, url_for
from config import Config
from flask_bootstrap import Bootstrap


# Register Extensions
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Extensions
    bootstrap.init_app(app)

    # Blueprint Imports
    from app.dailybriefing import dailybriefing_bp
    app.register_blueprint(dailybriefing.dailybriefing_bp)

    from app.snippetimport import snippetimport_bp
    app.register_blueprint(snippetimport.snippetimport_bp)

    return app