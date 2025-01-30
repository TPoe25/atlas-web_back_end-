#!/usr/bin/env python3
"""
Defines a Most Recently Used (MRU) caching system.
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class that implements a Most Recently Used (MRU) caching system.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initialize the MRU cache.
        Calls the parent class constructor and initializes an empty MRU queue.
        """
        super().__init__()
        self.mru_queue = []

    def put(self, key, item):
        """
        Add an item to the cache using the MRU algorithm.

        If cache is full, remove most recently used item before adding new item

        Parameters:
        key (str): The key to associate with the item in the cache.
        item (Any): The item to be stored in the cache.

        Returns:
        None

        Side effects:
        - Updates the cache_data dictionary with the new key-item pair.
        - Updates the mru_queue to reflect the most recently used items.
        - If cache full, remove most recently used item & print discard message
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru_queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.mru_queue.pop()
            del self.cache_data[discard]
            print("DISCARD:", discard)
        self.cache_data[key] = item
        self.mru_queue.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        If the key exists in the cache, move it to the front of the MRU queue.

        Parameters:
        key (str): The key to look up in the cache.

        Returns:
        Any: The item associated with the key, or None if not found.
        """
        if key in self.cache_data:
            self.mru_queue.remove(key)
            self.mru_queue.append(key)
            return self.cache_data[key]
        return None
