#!/usr/bin/python3
""" 
a function that returns True if the object is an instance 
of a class that inherited (directly or indirectly) from 
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class
    Args:
        obj: object to be checked for inheritance
        a_class: the class we are to check if it's inherited from
    Return:
        True: if obj inherited from a_class
        False: otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
