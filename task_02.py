#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Docstring."""


def bool_to_str(bval):
    """This is a function that prints 'Yes' or 'No' based on a given
       Truthiness value.

    Args:
        bval (boolean): True or False

    Returns:
        'Yes' or 'No'

    Example:
        >>> bool_to_str(True)
        'Yes'

    """

    if bval:
        response = 'Yes'
    else:
        response = 'No'
    return response
