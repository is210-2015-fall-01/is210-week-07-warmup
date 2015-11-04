#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 warmup Task 01"""


def fibonacci(maxint):
    """This module will build a Fibonacci sequence.

    Fibonacci sequence is a set of numbers that starts with a one or a zero,
    followed by a one, and proceeds based on the rule that each number is equal
    to the sum of the preceding two numbers.

    Args:
        Max(int): maxint parameter.

    Returns:
        generate lists of sequence.

    Examples:
        >>> import task_01.py
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]
    """

    lists = []
    lastnum, curnum = 1, 0

    while curnum < maxint:
        lists = lists + [curnum]
        lastnum, curnum = curnum, lastnum + curnum
    return lists
