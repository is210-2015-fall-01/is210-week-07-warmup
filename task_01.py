#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series."""

def fibonacci(maxint):
    """
    Args:
        maxint
    Returns:
    Examples:
    
    """
    a, b = 0, 1
    while b<maxint:
        print(b)
        a, b = b, a+b
