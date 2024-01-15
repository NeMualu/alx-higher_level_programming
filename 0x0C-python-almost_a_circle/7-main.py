#!/usr/bin/python3
""" Demonstrating the update method in the Rectangle class """

# Importing Rectangle class from models
from models.rectangle import Rectangle

def main():
    # Creating a Rectangle instance
    rect_instance = Rectangle(10, 10, 10, 10)
    print(rect_instance)

    # Updating only the ID of the Rectangle
    rect_instance.update(89)
    print(rect_instance)

    # Updating the ID and width of the Rectangle
    rect_instance.update(89, 2)
    print(rect_instance)

    # Updating the ID, width, and height of the Rectangle
    rect_instance.update(89, 2, 3)
    print(rect_instance)

    # Updating the ID, width, height, and x-coordinate of the Rectangle
    rect_instance.update(89, 2, 3, 4)
    print(rect_instance)

    # Updating all properties of the Rectangle
    rect_instance.update(89, 2, 3, 4, 5)
    print(rect_instance)

# Executing the main function if this script is run directly
if __name__ == "__main__":
    main()

