#!/usr/bin/env python3
""" FIFOCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO algorithm
    """
    def __init__(self):
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        """ get an item  by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
