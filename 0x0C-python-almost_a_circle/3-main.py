#!/usr/bin/python3
""" Demonstrating area calculation in Rectangle class """

# Importing the Rectangle class
from models.rectangle import Rectangle

def demonstrate_area_calculation():
    # Creating Rectangle instances
    rect_one = Rectangle(3, 2)
    rect_two = Rectangle(2, 10)
    rect_three = Rectangle(8, 7, 0, 0, 12)

    # Printing the area of each Rectangle
    print(rect_one.area())
    print(rect_two.area())
    print(rect_three.area())

# Run the demonstration function if this is the main script
if __name__ == "__main__":
    demonstrate_area_calculation()

