#!/usr/bin/env python3

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        item: self.cache_data
        if key or item is None:
            return None
        if self.cache[key] is item:
            return self.cache_data
        
    def get(self, key):
        if key is self.cache_data:
            print(self.cache_data[key])
