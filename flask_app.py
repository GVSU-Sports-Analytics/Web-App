from flask import Flask
from blueprints.about import about
from blueprints.baseball import bsbl
from blueprints.softball import softball
from blueprints.football import football
from blueprints.basketball import basketball
from blueprints.index import index

# import os
# import mysql.connector

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
    app.register_blueprint(softball)


# need to configure mysql database connection properly still

if __name__ == "__main__":
    register_blueprints()
    app.run(
        debug=True,
    )
