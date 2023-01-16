import sqlite3


def config_db():
    """
    For now, while we are using sqlite
    for devlopment purposes we are going to
    be using the absolute path of the db located
    in the GV-Crawler repo
    :return:
    """
    db = sqlite3.connect("/home/jensen/Documents/projects/gvsu-app/GV-Crawler/data/gvsac.db")
    return db


def de_tuple(l):
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


def column_names(cursor: sqlite3.Cursor, tbl_name: str):
    r = cursor.execute(f"SELECT * FROM {tbl_name};")
    return de_tuple(r.description)


def query(cursor: sqlite3.Cursor, qstring: str):
    r = cursor.execute(qstring)
    return r.fetchall()


def map_cols2rows(cols: list[str], rows: list[tuple]) -> dict:
    return
