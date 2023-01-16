from dataclasses import dataclass, field
from flask import Flask, Blueprint
import sqlite3


@dataclass
class App:
    name: str
    port: int
    template_path: str
    static_path: str

    _db: sqlite3
    _cursor: sqlite3.Cursor

    _blueprints: list[Blueprint] = field(
        default_factory=lambda: []
    )

    @property
    def Name(self) -> str:
        return self.name

    @property
    def Port(self) -> int:
        return self.port

    @property
    def Database(self):
        return self._db

    @property
    def Cursor(self):
        return self._cursor

    def add_blueprints(self, *blueprints):
        for bp in blueprints:
            self._blueprints.append(bp)

    def config_blueprints(self, app: Flask):
        """
        Creates a Flask instance and
        then registers the blueprints to
        that specific instance
        """
        for bp in self._blueprints:
            app.register_blueprint(bp)

    def run(self):
        app = Flask(
            self.Name,
            static_folder=self.static_path,
            template_folder=self.template_path
        )
        print(__name__)
        self.config_blueprints(app)
        app.run(
            debug=True,
            port=self.port
        )
        self.Database.close()
        self.Cursor.close()
