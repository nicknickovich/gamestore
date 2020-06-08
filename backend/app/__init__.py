import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db = SQLAlchemy()
api_restful = Api()


def create_app(config_file):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    with app.app_context():
        app.config.from_pyfile("config.py")
        environment = os.getenv("FLASK_ENV")
        if environment == "production":
            app.config.from_pyfile("prod.py")
        elif environment == "development":
            app.config.from_pyfile("dev.py")
        elif environment == "testing":
            app.config.from_pyfile("test.py")

        db.init_app(app)

        from app.controllers import main
        from app.api import api

        app.register_blueprint(main)
        app.register_blueprint(api)

        api_restful.init_app(app)

    return app
