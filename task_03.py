#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Words in a speech. Perform lexicographical analysis."""


import decimal


def lexicographics(to_analyze):
    """This function evaluates from truthiness or falsiness.

    Args:
        to_analyze(int): required string

    Returns:
        tuple: with 3-values
            (
            int1=max number of words per line,
            int2=min number of words per line,
            decimal=average number of words per line
            )

    Examples:
        >>> import task_03
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    linesplit = to_analyze.splitlines()
    my_val = []

    for words in linesplit:
        my_val.append(len(words.split()))
        maxvar = max(my_val)
        minvar = min(my_val)
        avgvar = decimal.Decimal(sum(my_val))/len(linesplit)
    return(maxvar, minvar, avgvar)
