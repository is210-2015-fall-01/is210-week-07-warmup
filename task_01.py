#!user/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series"""

def fibonacci(maxint):
    """ Returns Fibonacci sequence as list.
    Arguments:
        maxint (int) number indicating where the loop should end
    Returns:
        list of numbers in fibonacci sequence up to maxint number
    Examples:
        fibonacci(100)
        >>>[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    a, b = 0, 1
    listresults = []

    while b < maxint:
        listresults.append(b)
        a, b = b, a + b
    return listresults
