#!/usr/bin/python3
""" Script demonstrating JSON serialization and deserialization in Rectangle class """

# Importing Rectangle class from models module
from models.rectangle import Rectangle

def main():
    # Sample list of dictionaries
    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]

    # Convert list of dictionaries to JSON string
    json_list_input = Rectangle.to_json_string(list_input)

    # Convert JSON string back to a list of dictionaries
    list_output = Rectangle.from_json_string(json_list_input)

    # Displaying the results
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()

