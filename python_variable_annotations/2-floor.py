#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating-point
number.
"""

import math


def floor(n: float) -> int:
    """
    Computes the floor of a floating-point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to the given number.
    """
    return math.floor(n)
