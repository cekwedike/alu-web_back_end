#!/usr/bin/env python3
"""
Module that contains a function that
safely gets value from dictionary
with appropriate typing
"""
from typing import Mapping, TypeVar, Union, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary with typing support.

    Args:
        dct (Mapping): A dictionary-like object
        key (Any): Key to look up in the dictionary
        default (Union[T, None]): Default value to return if key not found, 
        defaults to None

    Returns:
        Union[Any, T]: Value from dictionary if key exists,
                       otherwise returns default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
