from flask import Flask

from blueprints.baseball import baseball
from blueprints.index import index
from register import register_blueprints, config_db

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

register_blueprints(
    index,
    baseball,
    app=app,
)


if __name__ == "__main__":
    #  gunicorn --bind :3000 --workers 1 --threads 8 --timeout 0 app:app
    app.run(
        debug=True,
        port=8080,
    )
