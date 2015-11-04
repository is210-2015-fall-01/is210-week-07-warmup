#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Yes or no truthy or falsy"""


def bool_to_str(bval):
    """Determines truthy or falsy

    Args:
        bval(boolean): Input boolean

    Returns:
        str: 'Yes' or 'No'

    Examples:
        >>> bool_to_str(True)
        'Yes'
    """
    if bval:
        return 'Yes'
    else:
        return 'No'
