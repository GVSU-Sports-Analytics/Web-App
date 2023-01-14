from flask import Flask, request, redirect
from blueprints.baseball import baseball
from blueprints.softball import softball
from blueprints.football import football
from blueprints.basketball import basketball
from blueprints.index import index
from register import register_blueprints

import json
import requests

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

register_blueprints(
    index,
    baseball,
    football,
    basketball,
    softball,
    app=app,
)




if __name__ == "__main__":
    #  gunicorn --bind :3000 --workers 1 --threads 8 --timeout 0 app:app
    app.run(
        debug=True,
        host="0.0.0.0"
    )
