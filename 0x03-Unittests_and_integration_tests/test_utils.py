#!/usr/bin/env python3
"""This module defines the TestMemoize class."""
from utils import access_nested_map, get_json
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize and patch"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test suits for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test suits for access_nested_map raises keyerror """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestJson(unittest.TestCase):
    """mocks the get_json function"""
    def test_get_json(self):
        """mocks the get_json function without making actuall api
        calls
        """
        with patch('utils.get_json', Mock) as mock_of_get_json:
            mock_of_get_json.return_value = {"payload": True}
            mock_of_get_json.return_value = {"payload": False}
