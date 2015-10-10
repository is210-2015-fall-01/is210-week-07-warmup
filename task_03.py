#! usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week 7 warmup task_03."""

import decimal


def lexicographics(to_analyze):
    """This function will use for loop to construct simple data.

    This function will return maximum, minimum, and average length of words
    as well as constructing simple data set.

    Args:
        to_analyze(str): loop through data.

    Returns:
        returns max, min, and avarge lenth.

    Example:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """

    length = to_analyze.split('\n')
    data = []

    for word in length:
        words = len(word.split())
        data.append(words)
    return (max(data), min(data), sum(data)/decimal.Decimal(len(data)))
