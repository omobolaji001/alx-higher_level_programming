#!/usr/bin/python3
"""
    a function that returns the list of available
    attributes and methods of an object.
"""


def lookup(obj):
    """ retuns list of methods """
    return dir(obj)
