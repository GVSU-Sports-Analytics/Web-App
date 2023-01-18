from flask import render_template
from framework.page import Page
from data.db import unique_sports

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
