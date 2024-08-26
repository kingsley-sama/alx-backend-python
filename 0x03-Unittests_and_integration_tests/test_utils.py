#!/usr/bin/python3
"""This module defines the TestMemoize class."""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path:
                               Sequence, expected_output: Any):
        """test suits for access_nested_map
        """
        result: Any = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)


test = TestMemoize()
