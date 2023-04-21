#!/usr/bin/env python3
"""LRU caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Defines the LRU Cache"""

    def __init__(self) -> None:
        """Initializes the class instance"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            popped_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(popped_key)
            print("DISCARD: {}".format(popped_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            v = self.cache_data.pop(key)
            self.cache_data[key] = v
        return self.cache_data.get(key)
