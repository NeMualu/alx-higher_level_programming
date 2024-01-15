#!/usr/bin/python3
""" Main script to demonstrate Rectangle class functionality """

# Importing Rectangle class from models module
from models.rectangle import Rectangle

def main():
    # Creating two Rectangle instances
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)

    # Saving instances to a file named Rectangle.json
    Rectangle.save_to_file([r1, r2])

    # Reading and printing the content of Rectangle.json
    with open("Rectangle.json", "r") as file:
        print(file.read())

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()

