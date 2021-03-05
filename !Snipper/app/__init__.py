from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# Register Extensions
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    # Blueprint Imports
    from app.authentication import authentication_bp
    app.register_blueprint(authentication.authentication_bp)
    
    from app.dailybriefing import dailybriefing_bp
    app.register_blueprint(dailybriefing.dailybriefing_bp)

    from app.snippetimport import snippetimport_bp
    app.register_blueprint(snippetimport.snippetimport_bp)

    return app


from app import models