from flask import Blueprint, render_template
from register import config_db
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
    db = config_db()
    cur = db.cursor()
    tables = table_names(cur, "baseball")
    cur.close(), db.close()
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
    db = config_db()
    cur = db.cursor()
    data = query(cur, f"SELECT * FROM baseball_roster_{year};")
    cols = column_names(cur, f"baseball_roster_{year}")
    print(cols)
    return render_template(
        "year.html",
        sport="Baseball",
        year=year,
        data=data,
    )


@baseball.route("/baseball/<year>/<player_name>")
def _player(year, player_name) -> str:
    return render_template(
        "player.html",
        sport="Baseball",
        player=player_name,
        data=data,
    )
