#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected output"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for get_json"""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test get_json with mock requests.get"""
        test_url = "https://api.example.com/data"
        test_payload = {"key": "value"}

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize"""

    def test_memoize(self):
        """Test memoization of method calls"""

        class TestClass:
            """Dummy class to test memoize"""

            def __init__(self):
                self.call_count = 0

            @memoize
            def a_method(self):
                """Method to test memoization"""
                self.call_count += 1
                return self.call_count

        instance = TestClass()

        self.assertEqual(instance.a_method(), 1)
        self.assertEqual(instance.a_method(), 1)  # Should return cached value
        self.assertEqual(instance.a_method(), 1)  # Still cached, no increment


if __name__ == "__main__":
    unittest.main()
