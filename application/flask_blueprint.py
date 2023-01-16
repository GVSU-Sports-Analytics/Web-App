from dataclasses import dataclass
from flask import Blueprint



@dataclass
class BluePrint:
    name: str
    static_path: str
    template_path: str
    db: sqlite3
    cur: sqlite3.Cursor

    @property
    def Name(self) -> str:
        return self.name

    @property
    def Static(self) -> str:
        return self.static_path

    @property
    def Template(self) -> str:
        return self.template_path

    def config(self):
        self._blueprint = Blueprint(
                self.Name,
                static_folder=self.Static,
                template_folder=self.Template,
            )
    










