from flask import Flask
import os

import pymysql


def config_db():
    user_name = os.environ["GVAPP_USERNAME"]
    password = os.environ["GVAPP_PASSWORD"]
    host = os.environ["GVAPP_HOST"]

    db = pymysql.connect(
        host=host,
        user=user_name,
        password=password
    )
    return db


def register_blueprints(*args, app: Flask) -> None:
    for bp in args:
        app.register_blueprint(bp)
