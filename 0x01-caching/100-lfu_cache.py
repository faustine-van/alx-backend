#!/usr/bin/env python3
""" BasicCaching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LRUCache algorithm
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = {}

    def put(self, key, item):
        """add an item into the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.count[key] += 1
            # self.cache_data.pop(key)
            self.cache_data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_val = min(self.count.values())
                min_keys = [k for k, v in self.count.items() if v == min_val]
                if len(min_keys) > 1:
                    for k in self.cache_data.keys():
                        if k in min_keys:
                            discarded_key = k
                            self.cache_data.pop(discarded_key)
                            self.count.pop(discarded_key)
                            break  # break after removing first matching key
                else:
                    discarded_key = min_keys[0]
                    self.cache_data.pop(discarded_key)
                    self.count.pop(discarded_key)
                print(f'DISCARD: {discarded_key}')
            self.cache_data[key] = item
            self.count[key] = 1
            self.cache_data.move_to_end(key)

    def get(self, key):
        """get an item from cache or None if not found"""
        if key is None or key not in self.cache_data:
            return None
        else:
            self.count[key] += 1
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
