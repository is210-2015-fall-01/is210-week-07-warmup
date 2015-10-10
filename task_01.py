#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My good docstring."""


def fibonacci(maxint):
    """This is a function that print fibonacci numbers up to a defined
       maxint value.

    This function has the purpose of demonstrating the while loop. It
    generates a series of fibonacci numbers up to a defined maxint value.

    Args:
        maxint (int): Top range of the sequence

    Returns:
        A series of finonacci numbers.

    Example:
        >>> task_01.fibonacci(20)
        [1, 1, 2, 3, 5, 8, 13] 3)

    """

    mylist = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        mylist.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    print mylist
