from flask import Blueprint, render_template

football = Blueprint(
    "football",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@football.route("/football")
def _football() -> render_template:
    return render_template(
        "sport.html",
        sport="GVSU Football"
    )
