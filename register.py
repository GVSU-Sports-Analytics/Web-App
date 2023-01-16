from flask import Flask
import sqlite3


def register_blueprints(*args, app: Flask) -> None:
    for bp in args:
        app.register_blueprint(bp)


def config_db():
    """
    For now, while we are using sqlite
    for devlopment purposes we are going to
    be using the absolute path of the db located
    in the GV-Crawler repo
    :return:
    """
    db = sqlite3.connect("/home/jensen/Documents/projects/gvsu-app/GV-Crawler/data/gvsac.db")
    return db
