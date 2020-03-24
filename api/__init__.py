from flask import Flask, request

from api.blueprints import health, alert


def create_app(config=None):
    config = config if config is not None else {}

    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    app.config.from_mapping(config)

    app.register_blueprint(health.bp)
    app.register_blueprint(alert.bp)

    return app
