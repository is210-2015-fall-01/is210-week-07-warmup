#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


def bool_to_str(bval):
    """use of the if statement by creating a small function that can return a
      'yes' or 'no' value equivalent of truthy or falsy values

    Args:
         a boolean or boolean-like
         value that can be evaluated for truthiness or falsiness

    Returns:
         Return the string, 'Yes' otherwise, return the string 'No'
    """

    if bval:
        your_answer = 'Yes'
    else:
        your_answer = 'No'
    return your_answer
