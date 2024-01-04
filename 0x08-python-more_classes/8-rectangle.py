#!/usr/bin/python3
"""Module for Rectangle class definition."""

class Rectangle:
    """Defines a rectangle.

    Class Attributes:
        instance_count (int): Tracks the number of Rectangle instances.
        drawing_symbol (any): Symbol used for graphical representation.
    """

    instance_count = 0
    drawing_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Parameters:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
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
        """Computes the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines the larger of two Rectangles based on area.

        Parameters:
            rect_1 (Rectangle): First rectangle for comparison.
            rect_2 (Rectangle): Second rectangle for comparison.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError("Arguments must be instances of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Generates a string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = [str(self.drawing_symbol) * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Provides a formal representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Executes actions upon Rectangle instance deletion."""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")

