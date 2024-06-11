# .\resources\utils\cursor_util.py
from django.db import connections


class CursorUtil:
    _db_cursors = {}

    @classmethod
    def get_cursor(cls, db: str):
        if db not in cls._db_cursors:
            cls._db_cursors[db] = connections[db].cursor()
        return cls._db_cursors[db]

    @classmethod
    def execute(cls, query: str, params: tuple | list = None, try_fetch: bool = True, db: str = "default"):
        cursor = cls.get_cursor(db)
        try:
            cursor.execute(query, params)
            resp = cursor.fetchall() if try_fetch else None
            return resp
        finally:
            cursor.close()
