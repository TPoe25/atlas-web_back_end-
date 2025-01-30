#!/usr/bin/env python3
"""
BasicCache module defines a basic caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class defines basic caching system w/o limit
    Methods:
        put(key, item):
            Add an item to the cache.
        get(key):
            Retrieve item from the cache by key."""
    def put(self, key, item):
        """
        Put an item into the cache.
        Args:
            self: instance of BasicCache class
            key: The key to identify the item in the cache.
            item: The value to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        returns the item in the cache

        Args:
            self: instance of BasicCache class
            key: key to the item in cache

        Returns:
            value of the item in cache
        """
        return self.cache_data.get(key)
