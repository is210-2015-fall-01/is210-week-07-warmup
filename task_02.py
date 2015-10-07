#!user/bin/env python
# -*- coding: utf-8 -*-
"""If and else"""


def bool_to_str(bval):
    """Check truty or falsy value of input.
    Arguments:
        bval (bool): any input to be test for truthy or falsy value
    Return:
        "Yes" if True, "No", if False
    Examples:
        bool_to_str([1, 2])
        >>>"Yes"
        bool_to_str(0)
        >>>"No"
    """
    truthy = "Yes"
    falsy = "No"
    if bval:
        bval = truthy
    else:
        bval = falsy
    return bval
