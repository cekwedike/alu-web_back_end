#!/usr/bin/env python3
"""
Module that contains a function that safely
returns the first element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence
    if it exists, None otherwise.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
