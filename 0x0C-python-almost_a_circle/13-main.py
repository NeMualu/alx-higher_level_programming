#!/usr/bin/python3
""" Demonstrating features of the Square class """

# Importing Square class from models module
from models.square import Square

def demonstrate_square():
    # Create a Square object
    square1 = Square(10, 2, 1)
    print(square1)
    # Convert the Square object to a dictionary
    dict_square1 = square1.to_dictionary()
    print(dict_square1)
    print(type(dict_square1))

    # Create another Square object
    square2 = Square(1, 1)
    print(square2)
    # Update the new square with the dictionary of the first
    square2.update(**dict_square1)
    print(square2)
    # Check if both squares are the same
    print(square1 == square2)

# Run the demonstration if this script is the main program
if __name__ == "__main__":
    demonstrate_square()

