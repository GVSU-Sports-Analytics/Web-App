from flask import render_template
from framework.flask_blueprint import Page


sport = Page(
    name="sport",
    import_name=__name__,
    static_path="static",
    template_path="template",
)


@sport.View.route("/<sport_name>")
def sport_page(sport_name) -> str:

    tables = sport.Cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table'; 
    """)

    return render_template(
        "sport.html",
        sport_name=f"GVSU {sport_name}",
        data=tables,
    )


@sport.View.route("/<sport_name>/<year>")
def year_page(sport_name, year) -> str:
    return render_template(
        "year.html",
        sport_name=sport_name,
        year=year,
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
        year=year
    )
