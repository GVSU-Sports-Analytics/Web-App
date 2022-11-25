from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/")
def index() -> str:
    return render_template(
        "index.html",
        date=datetime.now()
    )


@app.route("/home")
def home() -> str:
    return render_template(
        "home.html",
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get("PORT", 3000))
    )
