from flask import Blueprint, render_template

login = Blueprint(
    "login",
    __name__,
    template_folder="templates"
)


@login.route("/login", methods=["GET", "POST"])
def _login() -> str:
    return render_template(
        "login.html",
    )
