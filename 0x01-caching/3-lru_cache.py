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
            popped_key, v = self.cache_data.popitem()
            print("DISCARD: {}".format(popped_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
