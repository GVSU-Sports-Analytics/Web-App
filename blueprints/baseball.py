from flask import Blueprint, render_template

baseball = Blueprint(
    "baseball",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@baseball.route("/baseball")
def _baseball() -> str:
    return render_template(
        "sport.html",
        sport="GVSU Baseball"
    )
