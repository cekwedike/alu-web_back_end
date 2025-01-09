#!/usr/bin/env python3
"""
This module defines a function to return a tuple consisting of a string
and the square of an integer or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k and the second
    element is the square of v as a float.

    Args:
        k (str): The string to be included as the first element of the tuple.
        v (Union[int, float]): The value to be squared and returned as the
                                second element.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k and
                           the second element is the square of v as a float.
    """
    return (k, float(v**2))
