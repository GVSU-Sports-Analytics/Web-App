from flask import render_template
from framework.flask_blueprint import Page
from db import query, de_tuple, unique_sports

index = Page(
    name="index",
    import_name=__name__,
    static_path="static",
    template_path="templates",
)


@index.View.route("/")
def home_page() -> str:
    sports = unique_sports(index.Cursor)
    return render_template(
        "index.html",
        sports=sports
    )
