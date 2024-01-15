#!/usr/bin/python3
""" Example script demonstrating conversion to dictionary and JSON in Base class """

# Importing necessary classes from models module
from models.base import Base
from models.rectangle import Rectangle

def main():
    # Create a Rectangle instance
    rectangle_instance = Rectangle(10, 7, 2, 8)
    # Convert instance to dictionary
    rect_dict = rectangle_instance.to_dictionary()
    # Convert dictionary to JSON string
    json_str = Base.to_json_string([rect_dict])

    # Displaying the outputs
    print(rect_dict)
    print(type(rect_dict))
    print(json_str)
    print(type(json_str))

# Run the main function when script is executed
if __name__ == "__main__":
    main()

