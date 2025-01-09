#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return float(sum(mxd_lst))
