#!/usr/bin/python3
"""Module for defining the Student class."""

class Student:
    """Class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Constructs a Student instance.

        This method initializes a new Student with the given first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Converts the Student instance to a dictionary.

        This method returns a dictionary representation of the Student instance, 
        containing all its attributes.

        Returns:
            A dictionary representation of the student.
        """
        return self.__dict__

