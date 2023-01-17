import requests
import json
from flask import render_template
from framework.flask_blueprint import Page

index = Page(
    name="index",
    import_name=__name__,
    static_path="static",
    template_path="templates",
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
    # this got changed somehow
    return res.json()


@index.View.route("/")
def home_page() -> str:
    return render_template(
        "index.html",
    )
