from flask import Blueprint, render_template, request
from register import config_db
from db import table_names

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
    db = config_db()
    cur = db.cursor()
    tables = table_names(cur, "baseball")
    return render_template(
        "sport.html",
        sport="GVSU Baseball",
        data=tables
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
