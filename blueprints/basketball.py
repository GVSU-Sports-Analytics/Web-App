from flask import Blueprint, render_template

basketball = Blueprint(
    "Basketball",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@basketball.route("/basketball")
def _basketball() -> render_template:
    return render_template(
        "sport.html",
        sport="GVSU Basketball"
    )
