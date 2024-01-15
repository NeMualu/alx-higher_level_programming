#!/usr/bin/python3
""" Demonstration of the display feature in the Rectangle class """

# Import the Rectangle class from models
from models.rectangle import Rectangle

def show_rectangles():
    # Creating and displaying the first rectangle
    rect_one = Rectangle(2, 3, 2, 2)
    rect_one.display()

    print("---")

    # Creating and displaying the second rectangle
    rect_two = Rectangle(3, 2, 1, 0)
    rect_two.display()

# Executing the function when the script is the main program
if __name__ == "__main__":
    show_rectangles()
