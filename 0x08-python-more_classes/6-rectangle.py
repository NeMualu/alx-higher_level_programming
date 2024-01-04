#!/usr/bin/python3
"""Module to define a Rectangle class."""

class Rectangle:
    """A class to represent a rectangle.

    Class Attributes:
        instance_count (int): Tracks the count of Rectangle instances.
    """

    instance_count = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        Rectangle.instance_count += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Provides a string representation of the Rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = ['#' * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns the formal string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Executed when a Rectangle instance is deleted."""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")

