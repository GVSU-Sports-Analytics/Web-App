from blueprints.index import index
from blueprints.sport import sport
from framework.flask_app import App
from db import config_db


if __name__ == "__main__":
    db = config_db()
    cur = db.cursor()

    app = App(
        name=__name__,
        port=8080,
        template_path="templates",
        static_path="static",
        _db=db,
        _cursor=cur,
    )

    app.add_blueprints(
        index,
        sport,
    )

    app.run()
