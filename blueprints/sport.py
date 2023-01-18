from flask import render_template
from framework.page import Page
from db import query_cols, query, table_names, unique_sports

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
    sports = unique_sports(sport.Cursor)
    return render_template(
        "sport.html",
        sport_name=sport_name,
        data=years,
        sports=sports
    )


@sport.View.route("/year/<sport_name>/<year>")
def year_page(sport_name, year) -> str:
    players = query(
        sport.Cursor,
        f"""SELECT player_name, image FROM {sport_name.lower()}_{year};"""
    )
    sports = unique_sports(sport.Cursor)
    return render_template(
        "year.html",
        sport_name=sport_name,
        year=year,
        data=players,
        sports=sports
    )


@sport.View.route("/gvsu_player/<sport_name>/<player_name>/<year>")
def player_page(sport_name, player_name, year) -> str:
    # sports is only needed for the nav bar
    sports = unique_sports(sport.Cursor)
    player_info = query_cols(
        sport.Cursor,
        f"SELECT player_name, height, weight FROM {sport_name}_{year} WHERE player_name='{player_name}';"
    )
    return render_template(
        "player.html",
        sport_name=sport_name,
        player_name=player_name,
        sports=sports,
        player_info=player_info
    )


@sport.View.route("/gvsu_player_year/<sport_name>/<player_name>/<year>")
def player_year_page(sport_name, player_name, year) -> str:
    sports = unique_sports(sport.Cursor)
    return render_template(
        "player.html",
        sport_name=sport_name,
        player_name=player_name,
        year=year,
        sports=sports,
    )
