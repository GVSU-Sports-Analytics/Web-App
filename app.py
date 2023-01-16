from blueprints.index import index
from blueprints.sport import sport
from application.flask_app import App
from db import config_db

db = config_db()
cur = db.cursor()

if __name__ == "__main__":
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
