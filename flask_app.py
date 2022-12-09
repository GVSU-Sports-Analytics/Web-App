
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.about import about
from blueprints.baseball.simulator import simulator
from blueprints.baseball.bsbl import bsbl
from blueprints.index import index
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


def register_blueprints() -> None:
    app.register_blueprint(index)
    app.register_blueprint(about)
    app.register_blueprint(bsbl)
    app.register_blueprint(simulator)


#def config_db(db_name: str) -> None:
#    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
#    db = SQLAlchemy()
#    db.init_app(app)

register_blueprints()

