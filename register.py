from flask import Flask
import os


def register_blueprints(*args, app: Flask) -> None:
    for bp in args:
        app.register_blueprint(bp)
