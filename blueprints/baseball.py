from flask import Blueprint, render_template
from db import table_names, query, column_names

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
    return render_template(
        "sport.html",
        sport="GVSU Baseball",
    )


@baseball.route("/baseball/<year>")
def _year(year):
    """
    :param year:
    :return:
    """
    return render_template(
        "year.html",
        sport="Baseball",
        year=year,
    )


@baseball.route("/baseball/<year>/<player_name>")
def _player(year, player_name) -> str:
    return render_template(
        "player.html",
        sport="Baseball",
        player=player_name,
    )
