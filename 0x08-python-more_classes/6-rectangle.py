#!/usr/bin/python3
"""Module for defining a Rectangle class."""

class Rectangle:
    """Defines a class representing the characteristics of a rectangle.

    Class Attributes:
        instance_count (int): Tracks the number of instances.
    """

    instance_count = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        Rectangle.instance_count += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must not be negative")
        self._width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must not be negative")
        self._height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either side is 0.
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """Provides a string representation of the rectangle using '#' symbols.

        Returns:
            str: The string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""

        lines = []
        for i in range(self._height):
            lines.append('#' * self._width)
        return "\n".join(lines)

    def __repr__(self):
        """Provides the official string representation of the rectangle.

        Returns:
            str: The official string representation.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Handles the deletion of a Rectangle instance."""
        Rectangle.instance_count -= 1
        print("Bye rectangle...")

