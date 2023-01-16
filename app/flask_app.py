from dataclasses import dataclass, field
from flask import Flask, Blueprint


@dataclass
class App:
    name: str
    port: int

    _self: Flask = field(
            default_factory=lambda: Flask(__name__)
        )

    @property
    def name(self) -> str:
        return self.name

    @property
    def port(self) -> int:
        return self.port

    def config(blueprints: list[Blueprint]) -> None:
        return

    def run(self):
        return
