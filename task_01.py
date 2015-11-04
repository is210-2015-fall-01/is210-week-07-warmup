#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def fibonacci(maxint):
    """Build a Fibonacci sequence generator function with our while loop.

    Args:
        The upper bound of the sequence will be your maxint parameter.

    Returns:
        Return the newly generated sequence as a list.
    """
    lastnum, curnum = 0, 1
    newlist = [lastnum]
    while curnum < maxint:
        lastnum, curnum = curnum, lastnum+curnum
        newlist.append(lastnum)
    return newlist
