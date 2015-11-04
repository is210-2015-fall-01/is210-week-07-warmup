#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using if then else to generate boolean responses"""


def bool_to_str(bval):
    """This function will use if then else statement to return a boolean

    Args:
        It takes one argument, bval

    Returns:
        A boolean

    Examples:
        >>> import task_02
        >>> task_02.bool_to_str('')
        'No'
    """
    if bval:
        return_val = 'Yes'
    else:
        return_val = 'No'
    return return_val
