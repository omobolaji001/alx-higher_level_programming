#!/usr/bin/python3
""" a class that inherits from list """


class Mylist(list):
    """ implements sorted method for Mylist """

    def print_sorted(self):
        """ prints a list in sorted ascending order """
        print(sorted(self))
