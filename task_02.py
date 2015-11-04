#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


def bool_to_str(bval):
    """Explains fucntion.
    Args:
        bval (bool): boolean that can be evaluated for truthiness or falsiness
    Returns:
        'Yes if true, 'No' if false
    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
,       'Yes'
        >>> import task_02
        >>> task 02.bool_to_str('')
        'No'
    """
    if bval:
        return 'Yes'

    else:
        return 'No'
