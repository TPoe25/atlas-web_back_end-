#!/usr/bin/env python3
"""
exercise module
"""

import redis
import random
from typing import Union
from typing import Optional


class Cache:
    """Cache class to handle Redis operations"""

    def __init__(self):
        """Initialize the Cache with a Redis connection"""
        self.__redis_client = redis.Redis(host='localhost', port=6379, db=0,
                                        decode_responses=True)

    def save_data(self, key: str, value: str, time_seconds: Optional[int]
                  = None) -> bool:
        """
        Save data to Redis with an optional expiration time.

        Args:
            key (str): The key under which to store the value.
            value (str): The value to store.
            time_seconds (Optional[int]): Optional expiration time in seconds.

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        return self.redis_client.set(name=key, value=value, ex=time_seconds)
    def read_data(self, key: str) -> Optional[str]:
        """
        Read data from Redis.

        Args:
            key (str): The key to read the value from.

        Returns:
            Optional[str]: The value associated w/ the key, None if not found.
        """
        return self.redis_client.get(name=key)

    def store(self, value: Union[str, bytes, int, float]) -> str:
        """
        Store a value in Redis with a random key.
        Args:
            value (Union[str, bytes, int, float]): The value to store.
        Returns:
            str: The randomly generated key under which the value is stored.
        """
        key = str(random.randint(0, 2**63 - 1))
        self.redis_client.set(key, value)
        return key

    def count_up(self, key: str) -> int:
        """
        Increment the value of a key in Redis.

        Args:
            key (str): The key to increment.

        Returns:
            int: The new value after incrementing.
        """
        return self.redis_client.incr(name=key)
    
    def remove_data(self, key: str) -> int:
        """
        Remove data from Redis.

        Args:
            key (str): The key to remove.

        Returns:
            int: The number of keys removed (1 if the key existed, 0 if not).
        """
        return self.redis_client.delete(key)
