from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment


# Register Extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
moment = Moment()

# Flask-login @login.required auto redirect
login.login_view = 'authentication.login'
login.login_message = 'Please log in in order to access this page.'


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

    # Blueprint Imports
    from app.authentication import authentication_bp
    app.register_blueprint(authentication.authentication_bp)

    from app.dailybriefing import dailybriefing_bp
    app.register_blueprint(dailybriefing.dailybriefing_bp)

    from app.snippetlibrary import snippetlibrary_bp
    app.register_blueprint(snippetlibrary.snippetlibrary_bp)

    from app.snippetimport import snippetimport_bp
    app.register_blueprint(snippetimport.snippetimport_bp)

    from app.profile import profile_bp
    app.register_blueprint(profile.profile_bp)

    return app


from app import models