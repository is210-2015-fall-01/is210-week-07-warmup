#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""

import decimal


def lexicographics(to_analyze):
    """To create a simple for-loop to loop over a simple data construct.

    Args:
        to_analyze, a required string

    Returns:
        Return these values as a tuple.
    """

    lines = to_analyze.splitlines()
    var = []
    for words in lines:
        var.append(len(words.split()))
    return(max(var), min(var), decimal.Decimal(sum(var))/len(lines))
