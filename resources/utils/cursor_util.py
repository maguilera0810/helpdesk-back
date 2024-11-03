# .\resources\utils\cursor_util.py
from django.db import connections


class CursorUtil:

    @classmethod
    def execute(cls, query: str, params: tuple | list = None, try_fetch: bool = True, db: str = "default"):
        cursor = connections[db].cursor()
        try:
            cursor.execute(query, params)
            resp = cursor.fetchall() if try_fetch else None
            return resp
        finally:
            cursor.close()
