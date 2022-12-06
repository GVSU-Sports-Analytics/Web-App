from flask import Blueprint, render_template

bsbl = Blueprint(
    "bsbl",
    __name__,
    template_folder="templates"
)


@bsbl.route("/baseball")
def _baseball() -> str:
    return render_template(
        "baseball.html",
    )
