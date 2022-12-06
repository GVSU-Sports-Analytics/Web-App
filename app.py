from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from blueprints.login import login
from blueprints.about import about
from blueprints.simulator import simulator
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# register blueprints
app.register_blueprint(login)
app.register_blueprint(about)
app.register_blueprint(simulator)

# configure user database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)


# home page
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
