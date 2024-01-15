#!/usr/bin/python3
""" Script to demonstrate saving and loading objects using Rectangle and Square classes """

# Importing Rectangle and Square classes from models module
from models.rectangle import Rectangle
from models.square import Square

def main():
    # Creating and saving a list of Rectangle objects
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]
    Rectangle.save_to_file(list_rectangles_input)

    # Loading the list of Rectangle objects from the file
    list_rectangles_output = Rectangle.load_from_file()

    # Displaying the input and output rectangles
    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    # Creating and saving a list of Square objects
    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]
    Square.save_to_file(list_squares_input)

    # Loading the list of Square objects from the file
    list_squares_output = Square.load_from_file()

    # Displaying the input and output squares
    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
