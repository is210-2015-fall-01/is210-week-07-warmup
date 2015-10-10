#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week 7 warmup task_02."""


def bool_to_str(bval):
    """This function uses boolean statements and return boolean values.

    This function if statement by creating a small function that can return a
    'yes' or 'no' value equivalent of truthy or falsy values.

    Args:
        bval(boolean): booelan statement.

    Returns:
        if true returns true value else return false value.

    Examples:
        >>>import task_02
        >>> task_02.bool_to_str(True)
        'Yes'
        >>> task 02.bool_to_str('')
        'No'
    """

    if bval:
        myval = 'Yes'
    else:
        myval = 'No'
    return myval
