import sqlite3


def config_db():
    # while we are testing with the
    # sqlite3 db, you must have the Sidearm-Updater
    # repo installed alongside the Web-App in same dir
    path = "/Users/jensen/Documents/projects/Sidearm-Updater/data/gvsac.db"
    return sqlite3.connect(
        path,
        check_same_thread=False,
    )


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
