import requests
import json
from flask import (
    Blueprint,
    render_template
)

from datetime import datetime
import pytz

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

    # check the current time with the most
    # recent update in the database (that we dont have yet)
    # and if it has been 24 hours, update the data, and log
    # the most recent update to be the current eastern time
    etc = pytz.timezone("US/Eastern")
    time = datetime.now(etc)


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
    return res.json()


@index.route("/")
def _index() -> str:
    """
    Checks if it is time to update the data
    that we currently have, and if it is it
    will send a post request to our GV-Crawler API
    :return: Serves the home page
    """

    # might be an issue because this is run every time a user refreshes
    if check_update():
        data = update()
        print(data.keys())

    return render_template(
        "index.html",
    )
