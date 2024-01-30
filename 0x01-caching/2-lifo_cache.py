#!/usr/bin/env python3
""" BasicCaching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """FIFO algorithm
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add an item on cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ get an item  by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
