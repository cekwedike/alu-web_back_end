#!/usr/bin/env python3
"""
This module defines a function to create
a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float
    by the specified multiplier.

    Args:
        multiplier (float): The value by which the input
        float will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes
        a float and returns its
        product with the multiplier.
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
