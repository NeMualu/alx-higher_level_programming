#!/usr/bin/python3
""" Example demonstrating the use of the Rectangle class """

# Importing Rectangle from the models package
from models.rectangle import Rectangle

def main():
    # Creating Rectangle instances with different parameters
    rectangle_a = Rectangle(10, 2)
    print(rectangle_a.id)

    rectangle_b = Rectangle(2, 10)
    print(rectangle_b.id)

    rectangle_c = Rectangle(10, 2, 0, 0, 12)
    print(rectangle_c.id)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()

