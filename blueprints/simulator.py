from flask import Blueprint, render_template

simulator = Blueprint("simulator", __name__, template_folder="templates")


@simulator.route("/simulator")
def _simulator() -> str:
    return render_template(
        "simulator.html",
    )
