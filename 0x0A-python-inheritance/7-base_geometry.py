#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a value """
        if isinstance(value, int) == False:
            raise TypeError("<value> must be integer")
        if value <= 0:
            raise ValueError("<value> must be greater than 0")
