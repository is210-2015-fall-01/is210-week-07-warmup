#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w7 warmup task 02."""


def bool_to_str(bval):
    """Boolean value that takes on required argument.

    Args:
        bval(int): boolean-like value that evaluates truthiness
        and falsiness.

    Returns:
        Yes or no.

    Examples:
        >>>import task_02
        >>> task_02.bool_to_str(True)
    """

    if bval:
        val = 'Yes'
    else:
        val = 'No'
    return val
