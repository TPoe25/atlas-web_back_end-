#!/usr/bin/env python3
"""
exercise module
"""

import redis
import uuid
from typing import Union, Optional, Callable



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
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes,
                                                            int, float, None]:
        """
        Retrieve data from Redis by key and apply a function if provided.
        
        Args:
            self (Cache): The instance of the Cache class.
            key (str): The key to retrieve data from.
            fn (Optional[callable]): A function to apply to the retrieved data.
        
        Returns:
            Union[str, bytes, int, float]:The data, possibly transformed by fn
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key.
        
        args:
            self (Cache): The instance of the Cache class.
            key (str): The key to retrieve the string from. 
        Returns:
            Optional[str]: The string value retrieved from Redis, or None n/f. 
        
        This method decodes the bytes to a string using UTF-8 encoding.
        If the key does not exist, it returns None.
        It uses the get method with a lambda function to decode the bytes.
        The lambda function is used to convert the bytes to a string.       
        """    
        
        return self.get(key, fn= lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key.
        
        Args:
            self (Cache): The instance of the Cache class.
            key (str): The key to retrieve the integer from"""
        return self.get(key, fn=int)