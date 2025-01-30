#!/usr/bin/env python3

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    A class that implements a Last-In-First-Out (LIFO) caching system.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initialize the LIFOCache.
        Calls the parent class constructor and initializes a LIFO queue.
        """
        super().__init__()
        self.lifo_queue = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full, removes the most recently added item
        before adding the new item.

        Args:
            key: The key to identify the item in the cache.
            item: The value to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.lifo_queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.lifo_queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD:", discard)
        self.cache_data[key] = item
        self.lifo_queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists in the cache,
            None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_queue.remove(key)
        self.lru_queue.append(key)
        return self.cache_data[key]
