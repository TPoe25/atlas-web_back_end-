#!/usr/bin/env python3
"""Utility functions"""

import requests
from functools import wraps
from typing import Dict, Any, Tuple


def access_nested_map(nested_map: Dict, path: Tuple) -> Any:
    """Access a nested dictionary using a sequence of keys"""
    for key in path:
        if not isinstance(nested_map, dict) or key not in nested_map:
            raise KeyError(f"Key {key} not found in {nested_map}")
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Dict:
    """Fetch JSON from a URL"""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Decorator to cache method results"""
    @wraps(method)
    def wrapper(self):
        if not hasattr(self, f"_{method.__name__}"):
            setattr(self, f"_{method.__name__}", method(self))
        return getattr(self, f"_{method.__name__}")
    return wrapper
