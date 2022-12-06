from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from blueprints.about import about
from blueprints.baseball.simulator import simulator
from blueprints.baseball.bsbl import bsbl
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


def register_blueprints() -> None:
    app.register_blueprint(about)
    app.register_blueprint(bsbl)
    app.register_blueprint(simulator)


def config_db(db_name: str) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    db = SQLAlchemy()
    db.init_app(app)


@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
    )


if __name__ == "__main__":
    register_blueprints()
    config_db("sports.db")
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
