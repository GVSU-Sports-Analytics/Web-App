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
    _app: Flask = field(
        default_factory=lambda: Flask(__name__)
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

    @property
    def App(self):
        return self._app

    def add_blueprints(self, *blueprints):
        for bp in blueprints:
            self._blueprints.append(bp)

    def config(self):
        for bp in self._blueprints:
            self._app.register_blueprint(bp)

    def run(self):
        self.config()
        self._app.run(
            debug=True,
            port=self.port
        )
        self.Database.close()
        self.Cursor.close()
