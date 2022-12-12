from flask import Blueprint, render_template

softball = Blueprint(
    "softball",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@softball.route("/softball")
def _softball():
    return render_template(
        "sport.html",
        in_progress=True,
        sport="GVSU Softball"
    )
