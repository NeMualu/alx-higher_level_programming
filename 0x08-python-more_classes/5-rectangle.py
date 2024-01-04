#!/usr/bin/python3
"""Rectangle module containing the Rectangle class."""


class Rectangle:
    """Class to define a rectangle object."""

    def __init__(self, width=0, height=0):
        """Constructor to create a Rectangle instance.

        Parameters:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to retrieve the width of the Rectangle."""
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
        """Method to retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Provide a string representation of the Rectangle using '#' symbols."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_lines = ['#' * self.__width for _ in range(self.__height)]
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """Return the formal string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Display a message upon Rectangle instance deletion."""
        print("Bye rectangle...")

