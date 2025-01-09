#!/usr/bin/env python3
"""Zoom Array Module.

This module provides a function to create a zoomed array by duplicating
each element a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Create a zoomed array from a tuple.

    Args:
        lst: A tuple of integers to zoom
        factor: The number of times to repeat each element (default=2)

    Returns:
        List containing the zoomed array where each element is repeated
        based on the zoom factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
