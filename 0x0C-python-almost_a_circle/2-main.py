#!/usr/bin/python3
""" Script demonstrating error handling in Rectangle class """

# Importing Rectangle class
from models.rectangle import Rectangle

def main():
    # Testing invalid width type
    try:
        Rectangle(10, "2")
    except Exception as error:
        print("[{}] {}".format(type(error).__name__, error))

    # Testing invalid width value
    try:
        rect_instance = Rectangle(10, 2)
        rect_instance.width = -10
    except Exception as error:
        print("[{}] {}".format(type(error).__name__, error))

    # Testing invalid x type
    try:
        rect_instance = Rectangle(10, 2)
        rect_instance.x = {}
    except Exception as error:
        print("[{}] {}".format(type(error).__name__, error))

    # Testing invalid y value
    try:
        Rectangle(10, 2, 3, -1)
    except Exception as error:
        print("[{}] {}".format(type(error).__name__, error))

# Execute main function when script is run
if __name__ == "__main__":
    main()
