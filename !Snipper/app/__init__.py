from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    #app.config.from_object(config_class)

    # from app.dailybriefing import bp as dailybriefing_bp
    # app.register_blueprint(dailybriefing_bp)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app