#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series."""


def fibonacci(maxint):
    """
    Args:
        maxint (int): when loop ends

    Returns:
        list up to maxint number
    Examples:
        >>> fibonacci(50)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    lastnum, curnum = 0, 1
    numlist = [lastnum]

    while curnum < maxint:
        numlist.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return numlist
