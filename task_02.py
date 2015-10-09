#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""warm up task for week 07"""


def bool_to_str(bval):
    """This function evaluates boolean like values for truthiness or falsiness.

    Args:
        bval (int): boolean like value to be tested.

    Returns:
        'Yes' or 'No'

    Examples:
        >>> import task_02
        >>> task_02.bool_to_str('')
        'No'
    """

    if bval:
        var = 'Yes'
    else:
        var = 'No'
    return var
