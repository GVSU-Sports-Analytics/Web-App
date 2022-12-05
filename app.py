from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

db = SQLAlchemy()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sports.db"

db.init_app(app)


@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )

    # sqlite3.connect("data/sports.db")
