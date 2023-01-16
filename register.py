from flask import Flask
import sqlite3
import os


def register_blueprints(*args, app: Flask) -> None:
    for bp in args:
        app.register_blueprint(bp)


def config_db():
    db = sqlite3.connect("/home/jensen/Documents/projects/gvsu-app/GV-Crawler/data/gvsac.db")
    return db
