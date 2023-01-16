import sqlite3


def de_tuple(l: list[tuple]):
    things = []
    for t in l:
        for i in t:
            things.append(i)
    return things


def table_names(cursor: sqlite3.Cursor, filt: str) -> list[str]:
    tables = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )
    tables = de_tuple(tables.fetchall())
    return [tbl for tbl in tables if filt in tbl]
