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
    VAR1='Yes'
    if bval==True:
        VAR1='Yes'
    else:
        VAR1='No'
    return VAR1
