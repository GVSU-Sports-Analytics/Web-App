from flask import render_template
from framework.flask_blueprint import Page
from db import query, table_names, de_tuple


sport = Page(
    name="sport",
    import_name=__name__,
    static_path="static",
    template_path="template",
)


@sport.View.route("/<sport_name>")
def sport_page(sport_name) -> str:
    tables = table_names(
        sport.Cursor,
        sport_name.lower(),
    )
    years = [tbl.split("_")[-1] for tbl in tables]
    return render_template(
        "sport.html",
        sport_name=sport_name,
        data=years,
    )


@sport.View.route("/<sport_name>/<year>")
def year_page(sport_name, year) -> str:
    players = query(
        sport.Cursor,
        f"""SELECT player_name, image FROM {sport_name.lower()}_{year};"""
    )
    return render_template(
        "year.html",
        sport_name=sport_name,
        year=year,
        data=players,
    )


@sport.View.route("/<sport_name>/<player_name>")
def player_page(sport_name, player_name) -> str:
    return render_template(
        "player.html",
        sport_name=sport_name,
        player_name=player_name,
    )


@sport.View.route("/<sport_name>/<player_name>/<year>")
def player_year_page(sport_name, player_name, year) -> str:
    return render_template(
        "player.html",
        sport_name=sport_name,
        player_name=player_name,
        year=year,
    )
