#!/usr/bin/python3
""" Demonstrating the update method with named parameters in the Rectangle class """

# Importing Rectangle class from models
from models.rectangle import Rectangle

def main():
    # Creating a Rectangle instance
    rect_instance = Rectangle(10, 10, 10, 10)
    print(rect_instance)

    # Updating the height of the Rectangle using a named parameter
    rect_instance.update(height=1)
    print(rect_instance)

    # Updating the width and x-coordinate of the Rectangle using named parameters
    rect_instance.update(width=1, x=2)
    print(rect_instance)

    # Updating multiple properties of the Rectangle using named parameters
    rect_instance.update(y=1, width=2, x=3, id=89)
    print(rect_instance)

    # Updating the x-coordinate, height, y-coordinate, and width of the Rectangle using named parameters
    rect_instance.update(x=1, height=2, y=3, width=4)
    print(rect_instance)

# Executing the main function if this script is run directly
if __name__ == "__main__":
    main()

