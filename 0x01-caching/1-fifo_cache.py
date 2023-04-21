#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Defines the FIFO Cache"""
    
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
            del self.cache_data[popped_key]
            print("DISCARD: {}".format(popped_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
