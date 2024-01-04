#!/usr/bin/python3
"""Module for defining a Rectangle class."""

class Rectangle:
    """Class to model a rectangle.

    Class Variables:
        instance_count (int): Counter for the number of Rectangle instances.
        symbol (any): Character or string used for the rectangle representation.
    """

    instance_count = 0
    symbol = "#"

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
        """Accessor for the width of the Rectangle."""
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
        """Accessor for the height of the Rectangle."""
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
        """String representation of the Rectangle using the defined symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = [str(self.symbol) * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Formal string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Action performed upon deletion of a Rectangle instance."""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")

