#!/usr/bin/env python3

from base_caching import BaseCaching

def __init__(self):
    """
    Initialize the cache.
    """
    super().__init__()
    self.queue = []
class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.queue = item
        
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        (self.cache_data[key])
