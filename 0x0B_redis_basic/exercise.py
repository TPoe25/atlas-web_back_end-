#!/usr/bin/env python3
"""
exercise module
"""

import redis

import uuid
from typing import Union



class Cache:
    """Cache class to handle Redis operations"""

    def __init__(self):
        """Initialize the Cache with a Redis connection"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()
        
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key.
        
        Args:
            self (Cache): The instance of the Cache class.
            data (Union[str, bytes, int, float]): The data to store.
        
        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
