from flask import Blueprint, render_template

index = Blueprint(
    "index",
    __name__,
    static_folder="static",
    template_folder="templates"
)


@index.route("/")
def _index() -> str:
    return render_template(
        "index.html",
    )
