from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sports.db"

db = SQLAlchemy()
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
