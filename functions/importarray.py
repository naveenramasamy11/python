#!/usr/bin/env python3
"""Demonstrates the use of Python's built-in array module."""

from array import array


def create_int_array() -> array:
    return array("i", [1, 2, 3, 4, 5])


a = create_int_array()
print(a)
