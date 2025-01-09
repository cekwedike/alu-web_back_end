#!/usr/bin/env python3
"""
This module defines a function that takes an iterable of sequences and
returns a list of tuples. Each tuple contains a sequence from the iterable
and its corresponding length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples. Each tuple
    contains a sequence from the iterable and its length.
    Args:
        lst (Iterable[Sequence]): An iterable of sequences to process.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
