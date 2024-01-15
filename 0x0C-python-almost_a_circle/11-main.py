#!/usr/bin/python3
""" Demonstration of Square class methods """

# Importing Square class from the models module
from models.square import Square

def main():
    # Creating a Square object with initial size
    square_one = Square(5)
    print(square_one)

    # Updating the size using the update method
    square_one.update(10)
    print(square_one)

    # Updating with multiple parameters using update method
    square_one.update(1, 2)
    print(square_one)

    # Updating with named parameters using update method
    square_one.update(1, 2, 3)
    print(square_one)

    # Updating with named parameters and size, ignoring id
    square_one.update(1, 2, 3, 4)
    print(square_one)

    # Updating the position using named parameter
    square_one.update(x=12)
    print(square_one)

    # Updating size and position using named parameters
    square_one.update(size=7, y=1)
    print(square_one)

    # Updating size, id, and position using named parameters
    square_one.update(size=7, id=89, y=1)
    print(square_one)

# Executing the main function if the script is run directly
if __name__ == "__main__":
    main()

