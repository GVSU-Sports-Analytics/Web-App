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


@app.route("/endpoint", methods=["POST"])
def post():
    end_point_roster_data = {
        "URL": "https://gvsulakers.com",
        "DB": "n/a"
    }

    data = json.dumps(end_point_roster_data)
    res = requests.post(
        url="http://127.0.0.1:3000/",
        json=data
    )
    print(res.json())
    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
    )
