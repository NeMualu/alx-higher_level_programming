#!/usr/bin/python3
""" Demonstrating features of the Rectangle class """

# Import the Rectangle class from models package
from models.rectangle import Rectangle

def demonstrate_rectangle():
    # Initialize a Rectangle object
    rect1 = Rectangle(10, 2, 1, 9)
    print(rect1)
    # Convert the Rectangle object to a dictionary
    dict_rect1 = rect1.to_dictionary()
    print(dict_rect1)
    print(type(dict_rect1))

    # Create a new Rectangle object
    rect2 = Rectangle(1, 1)
    print(rect2)
    # Update the new rectangle with the dictionary of the first
    rect2.update(**dict_rect1)
    print(rect2)
    # Check if both rectangles are the same
    print(rect1 == rect2)

# Run the demonstration if this script is the main program
if __name__ == "__main__":
    demonstrate_rectangle()

