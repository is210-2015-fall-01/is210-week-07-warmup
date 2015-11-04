#! usr/bin/env python
# -*- coding: utf-8 -*-
"""Lexicographical analysis"""

import decimal
# import data


def lexicographics(to_analyze):
    """ Enter string to get max, min, and average.

    Args:
        to_analyze(str): Enter string to be calculated

    Returns:
        Tuple with max, min and average of entered words.

    Example:
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    my_value = []
    my_tup = to_analyze.split('\n')

    for item in my_tup:
        val = len(item.split())
        my_value.append(val)
    return (max(my_value), min(my_value),
            sum(my_value)/decimal.Decimal(len(my_value)))
