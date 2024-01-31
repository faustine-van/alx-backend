#!/usr/bin/env python3
""" BasicCaching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache algorithm
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add an item into the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # access the first key
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
        # add an item in dictionary
        self.cache_data[key] = item
        # move key to the end
        self.cache_data.move_to_end(key)

    def get(self, key):
        """get an item from cache or None if not found"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
