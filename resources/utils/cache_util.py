from functools import wraps

from django.core.cache import cache

from resources.utils.decode_util import DecodeUtil


class CacheUtil:

    @staticmethod
    def get_key(func_name: str, args: list, kwargs: dict, key_prefix: str = ""):
        """
        Genera un resumen para la clave de caché basado en el nombre de la función,
        los argumentos y el prefijo opcional.

        Parámetros:
        - func_name: Nombre de la función.
        - args: Argumentos posicionales de la función.
        - kwargs: Argumentos nombrados de la función.
        - key_prefix: Prefijo opcional para la clave de caché.

        Retorna:
        - Una cadena única que representa la clave de caché.
        """
        hashed_text = DecodeUtil.sha1(f"{func_name}{args}{kwargs}{key_prefix}")
        return f"{key_prefix}_{hashed_text}"

    @staticmethod
    def cache_data(key: str, func, timeout: int = 3600):
        """
        Almacena el resultado de una función en caché de manera directa.

        Parámetros:
        - key: Clave de caché específica.
        - func: Función cuyo resultado se almacenará en caché.
        - timeout: Tiempo en segundos antes de que expire el caché.
        """
        data = cache.get(key)
        if data is None:
            data = func()
            cache.set(key, data, timeout=timeout)
        return data

    @staticmethod
    def cache_decorator(timeout=3600, key_prefix=""):
        """
        Decorador para almacenar en caché el resultado de una función.

        Parámetros:
        - timeout: Tiempo en segundos antes de que expire el caché.
        - key_prefix: Prefijo de la clave del caché.
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                key = CacheUtil.get_key(func_name=func.__name__, args=args,
                                        kwargs=kwargs, key_prefix=key_prefix)
                return CacheUtil.cache_direct(key=key,
                                              func=lambda: func(
                                                  *args, **kwargs),
                                              timeout=timeout)
            return wrapper
        return decorator
