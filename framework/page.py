from flask import Blueprint
import sqlite3


class Page:
    def __init__(self, name, import_name, static_path, template_path):
        self.name: str = name
        self.import_name: str = import_name
        self.static_path: str = static_path
        self.template_path: str = template_path

        self.Assert()
        self._blueprint = Blueprint(
            name=self.Name,
            import_name=self.ImportName,
            static_folder=self.Static,
            template_folder=self.Template,
        )

    def Assert(self):
        assert (isinstance(self.Name, str))
        assert (isinstance(self.Static, str))
        assert (isinstance(self.Template, str))

    def __str__(self):
        return f"Flask page named \"{self.Name}\" defined @ \"{self.ImportName}\""

    def configure_database(self, db: sqlite3):
        self.db = db
        self.cur = db.cursor()

    @property
    def Name(self) -> str:
        return self.name

    @property
    def ImportName(self) -> str:
        return self.import_name

    @property
    def Static(self) -> str:
        return self.static_path

    @property
    def Template(self) -> str:
        return self.template_path

    @property
    def Database(self) -> sqlite3:
        assert self.db
        return self.db

    @property
    def Cursor(self) -> sqlite3.Cursor:
        assert self.cur
        return self.cur

    @property
    def View(self) -> Blueprint:
        return self._blueprint
