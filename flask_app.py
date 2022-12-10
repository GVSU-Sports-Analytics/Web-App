from flask import Flask
from blueprints.baseball import baseball
from blueprints.softball import softball
from blueprints.football import football
from blueprints.basketball import basketball
from blueprints.index import index
from flask_sqlalchemy import SQLAlchemy
from socket import gethostname
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
hostname = os.getenv("DB_HOST")
databasename = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=username,
    password=password,
    hostname=hostname,
    databasename=databasename,
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def register_blueprints() -> None:
    app.register_blueprint(index)
    app.register_blueprint(baseball)
    app.register_blueprint(football)
    app.register_blueprint(basketball)
    app.register_blueprint(softball)


if __name__ == "__main__":
    register_blueprints()
    db = SQLAlchemy(app)

    if 'liveconsole' not in gethostname():
        app.run(debug=True)
