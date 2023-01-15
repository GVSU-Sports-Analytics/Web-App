from flask import Blueprint, render_template

# for development only
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
    _2021 = data["_2021"]
    print(_2021)
    return render_template(
        "sport.html",
        in_progress=True,
        sport="GVSU Baseball",
        data=_2021,
    )
