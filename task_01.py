#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""warm up task for week 07"""


def fibonacci(maxint):
    """function that uses the fibonacci sequence.

    Args:
        maxint(int): integer that serves as the upper bound of the loop.

    Returns:
        the list of numbers in a fibonacci sequence.

    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """

    lastnum, curnum = 0, 1
    numlist = [lastnum]

    while curnum < maxint:
        numlist.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return numlist
