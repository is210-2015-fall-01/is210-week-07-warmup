#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculating max, min word counts and an average"""


import decimal
import data

TEXT = '''Hello.
My name is Saulat.
I love to cook new dishes.'''


def lexicographics(to_analyze):
    """This function will use a for loop and if statements.

    Args:
        It takes one argument, to_analyze

    Returns:
        Integers and a decimal floating point

    Examples:
        >>> (12, 5, 8.14)
    """
    lines = to_analyze.split('\n')
    total_words = 0
    count = 0
    for words in lines:
        word_count = words.split()
        no_of_words = len(word_count)
        total_words += no_of_words
        if count == 0:
            max_words = no_of_words
            min_words = no_of_words
        if no_of_words > max_words:
            max_words = no_of_words
        if no_of_words < min_words:
            min_words = no_of_words
        count += 1
    return (max_words, min_words,
            round(decimal.Decimal((float(total_words)/count)), 2))
print lexicographics(data.SHAKESPEARE)
