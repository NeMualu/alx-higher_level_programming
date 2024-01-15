#!/usr/bin/python3
""" Main script demonstrating usage of Square class """

# Importing the Square class from models module
from models.square import Square

def run_demo():
    # Creating a Square object and printing its details
    square_one = Square(5)
    print(square_one)
    print(square_one.size)

    # Updating the size of the square and printing again
    square_one.size = 10
    print(square_one)

    # Attempting to set an invalid size and handling the exception
    try:
        square_one.size = "9"
    except Exception as error:
        print("[{}] {}".format(error.__class__.__name__, error))

# Run the demonstration if this script is executed as the main program
if __name__ == "__main__":
    run_demo()

