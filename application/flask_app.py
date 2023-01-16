from dataclasses import dataclass, field
from application.flask_blueprint import Page
from flask import Flask
import sqlite3


@dataclass
class App:
    name: str
    port: int
    template_path: str
    static_path: str

    _db: sqlite3
    _cursor: sqlite3.Cursor

    _pages: list[Page] = field(
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

    def add_blueprints(self, *blueprints: Page):
        for bp in blueprints:
            self._pages.append(bp)

    def config_blueprints(self, app: Flask):
        """
        Creates a Flask instance and
        then registers the blueprints to
        that specific instance
        """
        for bp in self._pages:
            app.register_blueprint(bp.View)

    def run(self):
        app = Flask(
            self.Name,
            static_folder=self.static_path,
            template_folder=self.template_path
        )
        self.config_blueprints(app)
        app.run(
            debug=True,
            port=self.port
        )
        self.Database.close()
        self.Cursor.close()
