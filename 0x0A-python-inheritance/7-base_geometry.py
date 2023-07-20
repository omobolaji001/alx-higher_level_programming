#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a value
        
        Args:
            name: name of the instance variable
            value: value of the instance variable
        """
        if type(value) != int:
            raise TypeError("{} must be integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
