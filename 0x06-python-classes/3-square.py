#!/usr/bin/python3

class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2
