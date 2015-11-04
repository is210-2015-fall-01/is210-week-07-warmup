#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci sequence"""


def fibonacci(maxint):
    """Fibonacci sequence generator.

    Args:
        maxint(int): Random number

    Returns:
        list: Fibonacci sequence

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    sequence = []
    lastnum, curnum = 1, 0
    while curnum < maxint:
        sequence = sequence + [curnum]
        lastnum, curnum = curnum, lastnum + curnum
    return sequence
