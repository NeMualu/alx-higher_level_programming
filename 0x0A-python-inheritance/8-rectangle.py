#!/usr/bin/python3
"""Defines a Rectangle class, extending from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Creates a representation of a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Constructs a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

