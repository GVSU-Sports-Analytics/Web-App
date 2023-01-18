from dataclasses import dataclass, field
from framework.component import Component
from framework.page import Page
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

    _components: list[Component] = field(
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

    def add_components(self, *components: Component):
        for cp in components:
            self._components.append(cp)

    def config_blueprints(self, app: Flask):
        for page in self._pages:
            page.configure_database(self.Database)
            app.register_blueprint(page.View)

    def config_components(self):
        for cp in self._components:
            cp.configure_database(self.Database)

    def run(self):
        app = Flask(
            self.Name,
            static_folder=self.static_path,
            template_folder=self.template_path
        )

        self.config_components()
        self.config_blueprints(app)

        app.run(
            debug=True,
            port=self.port
        )

        self.Cursor.close()
        self.Database.close()
