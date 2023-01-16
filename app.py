from blueprints.index import index
from blueprints.baseball import baseball
from db import config_db
from application.flask_app import App

db = config_db()
cur = db.cursor()

if __name__ == "__main__":
    app = App(
        name=__name__,
        port=3000,
        template_path="templates",
        static_path="static",
        _db=db,
        _cursor=cur,
    )
    app.add_blueprints(
        index,
        baseball
    )
    app.run()
