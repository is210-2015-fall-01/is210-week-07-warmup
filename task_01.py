#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A list of the Fibonacci sequence numbers."""


def fibonacci(maxint):
    """Uses a list to calculate and hold the Fibonacci numbers

    Args:
        maxint: an integer that will serve as the upper bound of the loop

    Returns:
        If maxint is not an integer, returns an error message; else, returns
        fiblist: a list containing the Fibonacci sequence numbers

    Raises:
        TypeError: fibonacci() takes exactly 1 argument (0 given)

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>> fibonacci(40)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if not isinstance(maxint, int):
        return '!!! ERROR !!! fibonacci() accepts an integer argument only.'
    else:
        fiba = 0
        fibb = 1
        fiblist = [fiba, fibb]
        while fibb < maxint:
            fiba, fibb = fibb, fiba + fibb
            if fibb < maxint:
                fiblist.append(fibb)
        return fiblist
