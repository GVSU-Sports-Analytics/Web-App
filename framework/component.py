from flask import render_template
from typing import Callable
import sqlite3


class Component:
    def __init__(
            self,
            name: str,
            template_path: str,
            static_path: str,
            data: dict
    ):
        self.name: str = name
        self.data: dict = data
        self.static_path: str = static_path
        self.template_path: str = template_path

    @property
    def Name(self) -> str:
        return self.name

    @property
    def Template(self) -> str:
        return self.template_path

    @property
    def Data(self) -> dict:
        return self.data

    @property
    def Database(self):
        assert self.db
        return self.db

    @property
    def Cursor(self):
        assert self.cur
        return self.cur

    def configure_database(self, db: sqlite3):
        self.db = db
        self.cur = db.cursor()

    def Render(self):
        for key, val in self.Data.items():
            if isinstance(val, Callable):
                val(self.Cursor)
        return render_template(
            self.Template,
            data=self.Data
        )
