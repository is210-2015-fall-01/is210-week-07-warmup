#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The math behind the words."""

import decimal


def lexicographics(to_analyze):
    """This module does lexicographical analysis and computations.

    Args:
        to_analyze: a required string

    Returns:
        a tuple containing the max, min, and average words per line

    Raises:
        NameError: name 'x' is not defined (to_analyze must be a string)

    Examples:
        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4.0'))
        >>> import data
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    words = decimal.Decimal('0.0')
    lines = 0
    maxw = 0
    minw = len(to_analyze)
    avgw = 0
    linesplit = to_analyze.split('\n')
    for aline in linesplit:
        wordsplit = aline.split()
        words += len(wordsplit)
        lines += 1
        if len(wordsplit) > maxw:
            maxw = len(wordsplit)
        if len(wordsplit) < minw:
            minw = len(wordsplit)
    avgw = words / lines
    return (maxw, minw, avgw)
