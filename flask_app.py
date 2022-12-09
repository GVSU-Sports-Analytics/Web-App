from flask import Flask
import mysql.connector
from blueprints.about import about
from blueprints.baseball import bsbl
from blueprints.football import football
from blueprints.basketball import basketball
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
    app.register_blueprint(football)
    app.register_blueprint(basketball)


# does not connect from local machine
def config_db() -> mysql.connector.connect:
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        db=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD")
    )


# only if running on local machine
# comment out in prod
if __name__ == "__main__":
    register_blueprints()
    # con = config_db()
    app.run(
        debug=True,
    )
