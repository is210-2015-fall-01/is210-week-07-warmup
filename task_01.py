#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping through fibonacci numbers"""


my_int = 10
def fibonacci(my_int):
    """This function will loop to create a list of integers.

    Args:
        It takes one argument, my_int

    Returns:
        A list of integers

    Examples:
        >>>[0, 1, 1, 2, 3, 5, 8]
    """
    a,b = 0, 1
    my_list = [a]
    while b < my_int:
        my_list.append(b)
        a,b = b, a+b
       
    return my_list
print fibonacci(10)
