from flask import Flask
from blueprints.baseball import baseball
from blueprints.softball import softball
from blueprints.football import football
from blueprints.basketball import basketball
from blueprints.index import index
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


def config_db() -> None:
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    hostname = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_uri = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{db_name}"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def register_blueprints(*args) -> None:
    for bp in args:
        app.register_blueprint(bp)



if __name__ == "__main__":
	register_blueprints(
    	index, 
		baseball,
    	football, 
		basketball,
    	softball
	)

	config_db()
	db = SQLAlchemy(app)

	# python anywhere takes care of app.run()
	#app.run(debug=True)
