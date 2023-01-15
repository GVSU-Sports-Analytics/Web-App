import requests
import json
from flask import (
    Blueprint,
    redirect,
    render_template
)

index = Blueprint(
    "index",
    __name__,
    static_folder="static",
    template_folder="templates"
)


def check_update():
    """
    Condition to determine if it is
    time to call the GV-Crawler API or not
    :return:
    """
    return True


def update():
    """
    Sends a request to scrape new data from the
    GVSU roster webpage. Still need to make a condition
    for when this should be run
    :return: Gets back a json response containing the
    current and up to date gvsu roster data and uploads it
    to our database (that doesn't exist yet) and redirects all users
    to the home page
    """
    end_point_roster_data = {
        "URL": "https://gvsulakers.com",
    }
    data = json.dumps(end_point_roster_data)
    res = requests.post(
        # eventually this will be the actual url of the api endpoint
        url="http://0.0.0.0:3000/",
        json=data
    )
    print(res.json())
    return "sent request to api"


@index.route("/")
def _index() -> str:
    """
    Checks if it is time to update the data
    that we currently have, and if it is it
    will send a post request to our GV-Crawler API
    :return: Serves the home page
    """

    if check_update():
        update()

    return render_template(
        "index.html",
    )
