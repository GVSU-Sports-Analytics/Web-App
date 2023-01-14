from flask import Flask
import os


def config_db(app: Flask) -> None:
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    hostname = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_uri = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{db_name}"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def register_blueprints(*args, app: Flask) -> None:
    for bp in args:
        app.register_blueprint(bp)
