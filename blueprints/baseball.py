from flask import Blueprint, render_template

# for development only
# this update logic will be moved to the sidearm updater repo
from blueprints.index import update

baseball = Blueprint(
    "baseball",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@baseball.route("/baseball")
def _baseball() -> str:
    # get the baseball data from database
    # for now, we are calling the api whenever
    # the page refreshes so that we can at lease see the data
    # until we get a database
    data = update()
    return render_template(
        "sport.html",
        in_progress=True,
        sport="GVSU Baseball",
        data=data["_2021"],
    )
