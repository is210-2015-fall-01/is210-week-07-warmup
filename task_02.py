#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests if truthy or not."""


def bool_to_str(bval):
    """Returns a 'yes' or 'no' value equivalent of truthy or falsy values.

    Args:
        bval: a boolean/boolean-like value to be evaluated for truthiness/
        falsiness

    Returns:
        'Yes' if the bval is truthy or 'No' if bval is falsey

    Examples:
        >>> bool_to_str(True)
        'Yes'
        >>> bool_to_str('')
        'No'
        >>> bool_to_str([])
        'No'
    """
    torf = 'input error / try again'
    if bval:
        torf = 'Yes'
    else:
        torf = 'No'
    return torf
