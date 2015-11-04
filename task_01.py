#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def fibonacci(maxint):
    """Explains fucntion.
    Args:
        maxint (int): An integer that will serve an an upper bound in the loop
    Returns:
        A new list
    Examples:
        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """
    newlist = []
    firstval, secondval = 0, 1
    while secondval < maxint:
        newlist.append(secondval)
        firstval, secondval = secondval, firstval+secondval
    return newlist
