#!/usr/bin/python3
"""Module for defining a Rectangle class."""

class Rectangle:
    """A class to represent a rectangle.

    Class Attributes:
        instance_count (int): Tracks the number of Rectangle instances.
        symbol_for_display (any): Symbol used for the textual representation.
    """

    instance_count = 0
    symbol_for_display = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        Rectangle.instance_count += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves or sets the width of the Rectangle."""
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
        """Retrieves or sets the height of the Rectangle."""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines which Rectangle has a larger or equal area.

        Parameters:
            rect_1 (Rectangle): The first rectangle for comparison.
            rect_2 (Rectangle): The second rectangle for comparison.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with equal width and height.

        Parameters:
            size (int): The size for both width and height of the rectangle.
        """
        return cls(size, size)

    def __str__(self):
        """Provides a string representation of the Rectangle with symbols."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = [str(self.symbol_for_display) * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns a formal string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Actions to perform when a Rectangle instance is deleted."""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")

