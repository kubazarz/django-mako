from mako.cache import CacheImpl, register_plugin

_django_cache = None


class DjangoCacheImpl(CacheImpl):
    _cache_key = 'django-mako-%s'

    def __init__(self, cache):
        super(DjangoCacheImpl, self).__init__(cache)
        global _django_cache
        if _django_cache is None:
            from django.core.cache import cache as _django_cache
        self._django_cache = _django_cache

    def get_or_create(self, key, creation_function, **kwargs):
        cache_key = self._cache_key % key
        options = {}
        if 'timeout' in kwargs:
            options['timeout'] = kwargs['timeout']
        value = self._django_cache.get(cache_key)
        if value is None:
            value = creation_function()
            self._django_cache.set(cache_key, value, **options)
        return value

    def set(self, key, value, **kwargs):
        options = {}
        if 'timeout' in kwargs:
            options['timeout'] = kwargs['timeout']
        cache_key = self._cache_key % key
        self._django_cache.set(cache_key, value, **options)

    def get(self, key, **kwargs):
        cache_key = self._cache_key % key
        return self._django_cache.get(cache_key)

    def invalidate(self, key, **kwargs):
        cache_key = self._cache_key % self._cache_key
        self._django_cache.remove(cache_key)


register_plugin('djangomakocache', __name__, 'DjangoCacheImpl')
