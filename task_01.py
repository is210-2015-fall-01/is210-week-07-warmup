#!/usr/bin/env python
# -*- coding: utf-8  -*-
"""w7 warmup task 01."""


def fibonacci(maxint):
    """ This function creates a fibonacci sequence.

    Args:
        Max(int): will serve as the uper bound of the loop.

    Returns:
        A sequenced list of generated numbers.

    Examples:
        >>> import task_01.py
        >>> task_01.fibonacci(10)
    """

    lastnum, curnum = 0, 1
    list1 = [lastnum]

    while curnum < maxint:
        list1.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return list1
