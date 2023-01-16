from flask import render_template
from application.flask_blueprint import Page
from db import config_db

db = config_db()
cur = db.cursor()

sport = Page(
    name="sport",
    import_name=__name__,
    static_path="static",
    template_path="template",
    db=db,
    cur=cur
)


@sport.View.route("/<sport>")
def sport_page(sport) -> str:
    return render_template(
        "sport.html",
        sport=f"GVSU {sport}"
    )


@sport.View.route("/<sport>/<year>")
def year_page(sport, year) -> str:
    return render_template(
        "year.html",
        sport=sport,
        year=year,
    )


@sport.View.route("/<sport>/<player_name>")
def player_page(sport, player_name) -> str:
    return render_template(
        "player.html",
        sport=sport,
        player_name=player_name,
    )


@sport.View.route("/<sport>/<player_name>/<year>")
def player_year_page(sport, player_name, year) -> str:
    return render_template(
        "player.html",
        sport=sport,
        player_name=player_name,
        year=year
    )
