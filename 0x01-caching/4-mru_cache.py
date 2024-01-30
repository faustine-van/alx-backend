#!/usr/bin/env python3
""" BasicCaching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """FIFO algorithm
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add an item in cache"""
        if key is None or item is None:
            return  # Do nothing if key or item is None
        if key in self.cache_data:
            self.cache_data.pop(key)
        # check if cache is Full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Assign the new item to the dictionary
            discarded_key, _ = self.cache_data.popitem()
            print(f'DISCARD: {discarded_key}')
        # Assign the new item to the dictionary
        self.cache_data[key] = item
        # Move the key to the end to mark it as the most recently used
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ get an item  by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
