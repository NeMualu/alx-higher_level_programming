#!/usr/bin/python3
""" Script to demonstrate the instantiation of Rectangle objects """

# Import Rectangle class from models
from models.rectangle import Rectangle

def main():
    # Create a Rectangle instance with specific parameters
    rectangle_a = Rectangle(4, 6, 2, 1, 12)
    print(rectangle_a)

    # Create another Rectangle instance with a different set of parameters
    rectangle_b = Rectangle(5, 5, 1)
    print(rectangle_b)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()

