from django.core.cache import cache


class CacheUtil:

    @classmethod
    def cache_data(cls, key: str, func, timeout: int = 3600):
        data = cache.get(key)
        if data is None:
            data = func()
            cache.set(key, data, timeout=timeout)
        return data
