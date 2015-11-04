#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""warm up task 03 for week 07"""

import decimal


def lexicographics(to_analyze):
    """function that provides the max, min, and avr for length of words.

    Args:
        to_analyze (str): the string that you want to measure.

    Returns:
        max, min, and avr of words in a string file.

    Examples:
        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """

    lines = to_analyze.splitlines()
    var = []
    for words in lines:
        var.append(len(words.split()))
    return(max(var), min(var), decimal.Decimal(sum(var))/len(lines))
