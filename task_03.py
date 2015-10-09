#!user/bin/env python
# -*- coding: utf-8 -*-
"""Find max, min and avg words per line"""

import decimal


def lexicographics(to_analyze):
    """ calcule max, min, and avg words per line.
    Arguments:
        to_analyze(str): multi-line string of text
    Returns:
        lines with max, min wrds and avg words per line
    Examples:
        STRING = ('This the first line of a string in Python\n'
          'that has multiple lines, in fact there are three lines total\n'
          'and this is the last one.')
        lexicographics(STRING)
        >>>(11, 6, Decimal('8.666666666666666666666666667'))
        """
    maxline = 0
    avgline = 0
    to_analyze = to_analyze.split('\n')
    minline = len(to_analyze[0])
    for line in to_analyze:
        words = line.split()
        if len(words) > maxline:
            maxline = len(words)
        if len(words) < minline:
            minline = len(words)
        avgline += len(words)
    avgline = decimal.Decimal(avgline) / decimal.Decimal(len(to_analyze))

    return (maxline, minline, avgline)


STRING = ('This the first line of a string in Python\n'
          'that has multiple lines, in fact there are three lines total\n'
          'and this is the last one.')
