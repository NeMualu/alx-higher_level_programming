#!/usr/bin/python3
""" Example demonstrating the Square class and its functionalities """

# Importing Square class from models
from models.square import Square

def main():
    # Creating a Square instance with a size of 5
    square_one = Square(5)
    print(square_one)
    print(square_one.area())
    square_one.display()

    print("---")

    # Creating another Square instance with a size of 2 and position (2, 0)
    square_two = Square(2, 2)
    print(square_two)
    print(square_two.area())
    square_two.display()

    print("---")

    # Creating a third Square instance with a size of 3 and position (1, 3)
    square_three = Square(3, 1, 3)
    print(square_three)
    print(square_three.area())
    square_three.display()

# Running the main function when the script is executed directly
if __name__ == "__main__":
    main()

