import requests
import json
from flask import render_template
from application.flask_blueprint import Page
from db import config_db

db = config_db()
cur = db.cursor()


index = Page(
    name="index",
    import_name=__name__,
    static_path="static",
    template_path="templates",
    db=db,
    cur=cur,
)


# we are moving this logic out of the web application logic
# and into a process that will run once every 24 hours.
# calling the api directly from the application is not a great idea
def update():
    end_point_roster_data = {
        "URL": "https://gvsulakers.com",
    }
    data = json.dumps(end_point_roster_data)
    res = requests.post(
        # eventually this will be the actual url of the api endpoint
        url="http://0.0.0.0:3000/",
        json=data
    )
    return res.json(cur=db.cursor())


@index.View.route("/")
def home_page() -> str:
    return render_template(
        "index.html",
    )
