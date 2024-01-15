#!/usr/bin/python3
""" Script to demonstrate object creation from dictionary in Rectangle class """

# Importing the Rectangle class
from models.rectangle import Rectangle

def demonstrate_rectangle_creation():
    # Initializing a Rectangle object
    rect1 = Rectangle(3, 5, 1)
    # Converting the Rectangle object to a dictionary
    rect1_dict = rect1.to_dictionary()
    # Creating a new Rectangle object from the dictionary
    rect2 = Rectangle.create(**rect1_dict)

    # Displaying both Rectangle objects
    print(rect1)
    print(rect2)
    # Checking if both objects are the same object or have the same content
    print(rect1 is rect2)
    print(rect1 == rect2)

# Execute the function when the script is run
if __name__ == "__main__":
    demonstrate_rectangle_creation()

