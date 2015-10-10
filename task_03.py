#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""

import decimal


def lexicographics(to_analyze):
    maxnum = 0
    minimum = 0
    average = 0
    newlines = to_analyze.split('\n')
    for item in newlines:
        maxnum = max(item)
        minimum = min(item)
        average = decimal.Decimal(sum(item)) / len(newlines)
    return (maxnum, minimum, average)

