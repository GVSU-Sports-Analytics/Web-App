from flask import Blueprint, render_template, request

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
        sport="GVSU Baseball",
        data=data,
    )


@baseball.route("/baseball/<year>")
def _year(year):
    """
    :param year:
    :return:
    """
    data = update()[year]
    return render_template(
        "year.html",
        sport="Baseball",
        year=year,
        data=data,
    )


@baseball.route("/baseball/<year>/<player_name>")
def _player(year, player_name) -> str:
    data = update()[year][player_name]
    return render_template(
        "player.html",
        sport="Baseball",
        player=player_name,
        data=data,
    )
