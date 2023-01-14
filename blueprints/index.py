from flask import Blueprint, render_template

index = Blueprint(
    "index",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@index.route("/")
def _index() -> str:
    """
    Checks if it is time to update the data
    that we currently have, and if it is it
    will send a post request to our GV-Crawler API
    :return: Serves the home page
    """
    return render_template(
        "index.html",
    )
