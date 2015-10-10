#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Evaluates truthy or falsy."""


def bool_to_str(bval):
    """This fucntion evaluates from truthiness or falsiness.
    Args:
        bval(mixed): Can be True or another input like boolean
    Returns:
        boolean-like with yes or no
    Examples:
        >>> bool_to_str('')
        'No'
        >>> bool_to_str(True)
        'Yes'
    """
    if bval:
        varr = 'Yes'
    else:
        varr = 'No'
    return varr
