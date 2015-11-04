#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w7 warmup task 03."""

import decimal


def lexicographics(to_analyze):
    """This function provide the maximum, minimum,
        and average length of words.

    Args:
        to_anaylze(str): that calculates lenth.

    Returns:
        returns the max. minimum, and averages of words
        per line.

    Examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
            Hold on to that feeling.''')
            (5, 3, Decimal(4.0))
    """

    lines = to_analyze.splitlines()
    var = []
    for words in lines:
        var.append(len(words.split()))
    return (max(var), min(var), decimal.Decimal(sum(var))/len(lines))
