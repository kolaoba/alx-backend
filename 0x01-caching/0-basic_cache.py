#!/usr/bin/env python3
"""Basic Dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Defines a BaseCaching Class"""

    def __init__(self) -> None:
        """Initializes the class instance"""
        super().__init__()
        self.MAX_ITEMS = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
