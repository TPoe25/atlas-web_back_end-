#!/usr/bin/env python3

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    A class that implements a Least Recently Used (LRU) caching system.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initialize the LRU cache.
        Calls the parent class constructor and initializes an empty LRU queue.
        """
        super().__init__()
        self.lru_queue = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If cache full, remove least recently used item before adding new item.

        Args:
            key: The key to identify the item in the cache.
            item: The value to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.lru_queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.lru_queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD:", discard)
        self.cache_data[key] = item
        self.lru_queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        If item exists, moved to end of LRU queue as it's most recently used.

        Args:
            key: The key of the item to retrieve from the cache.

        Returns:
            The value associated with the key if it exists in cache, else None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_queue.remove(key)
        self.lru_queue.append(key)
        return self.cache_data[key]
