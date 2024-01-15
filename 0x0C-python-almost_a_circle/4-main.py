#!/usr/bin/python3
""" Script for demonstrating the display method in Rectangle class """

# Importing the Rectangle class
from models.rectangle import Rectangle

def display_rectangles():
    # Creating a Rectangle object and displaying it
    rectangle1 = Rectangle(4, 6)
    rectangle1.display()

    print("---")

    # Creating another Rectangle object and displaying it
    rectangle2 = Rectangle(2, 2)
    rectangle2.display()

# Executing the function when the script is run directly
if __name__ == "__main__":
    display_rectangles()

