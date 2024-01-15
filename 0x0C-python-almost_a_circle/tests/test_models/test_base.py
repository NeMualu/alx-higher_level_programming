#!/usr/bin/python3
"""
This module conducts unit testing for the Base class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A collection of test cases for the Base class.
    """

    def setUp(self):
        """
        Sets up the test environment before each test.
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Clean up actions after each test.
        """
        pass

    def test_nb_objects_private_attribute(self):
        """
        Checks if the nb_objects attribute is private.
        """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initial_value(self):
        """
        Verifies nb_objects is initialized to zero.
        """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_base_initialization(self):
        """
        Tests the initialization of a Base instance.
        """
        base_instance = Base()
        self.assertEqual(str(type(base_instance)), "<class 'models.base.Base'>")
        self.assertEqual(base_instance.__dict__, {"id": 1})
        self.assertEqual(base_instance.id, 1)

    def test_base_constructor(self):
        """
        Checks the constructor's argument handling.
        """
        with self.assertRaises(TypeError) as context:
            Base.__init__()
        self.assertIn("missing 1 required positional argument: 'self'", str(context.exception))

        with self.assertRaises(TypeError) as context:
            Base.__init__(self, 1, 2)
        self.assertIn("takes from 1 to 2 positional arguments but 3 were given", str(context.exception))

    def test_consecutive_ids(self):
        """
        Tests for consecutive IDs in successive Base instances.
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_id_synchronization(self):
        """
        Verifies synchronization between class and instance IDs.
        """
        base = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), base.id)

    def test_custom_id_assignment(self):
        """
        Tests custom ID assignment for Base instances.
        """
        custom_id_int = 98
        base_int = Base(custom_id_int)
        self.assertEqual(base_int.id, custom_id_int)

        custom_id_str = "FooBar"
        base_str = Base(custom_id_str)
        self.assertEqual(base_str.id, custom_id_str)

        custom_id_kwarg = 421
        base_kwarg = Base(id=custom_id_kwarg)
        self.assertEqual(base_kwarg.id, custom_id_kwarg)

    def test_to_json_string(self):
        """
        Tests the JSON string representation of dictionaries.
        """
        with self.assertRaises(TypeError) as context:
            Base.to_json_string()
        self.assertIn("missing 1 required positional argument: 'list_dictionaries'", str(context.exception))

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        # Various dictionary tests
        dict_sample = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(dict_sample)), len(str(dict_sample)))

        dict_various = [{"key1": "value1"}, {"key2": 2}, {"key3": None}]
        self.assertEqual(Base.to_json_string(dict_various), '[{"key1": "value1"}, {"key2": 2}, {"key3": null}]')

        # Test with Rectangle instances
        rect1 = Rectangle(10, 7, 2, 8)
        dict_rect1 = rect1.to_dictionary()
        json_rect1 = Base.to_json_string([dict_rect1])
        self.assertEqual(str([dict_rect1]).replace("'", '"'), json_rect1)

        # Test with Square instances
        square1 = Square(10, 7, 2)
        dict_square1 = square1.to_dictionary()
        json_square1 = Base.to_json_string([
        json_square1 = Base.to_json_string([dict_square1])
        self.assertEqual(str([dict_square1]).replace("'", '"'), json_square1)

    def test_from_json_string(self):
        """
        Tests the conversion from JSON string to the dictionary.
        """
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        dict_list = Base.from_json_string(json_str)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(dict_list, [{"id": 89, "width": 10, "height": 4}])

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """
        Tests the `create` class method.
        """
        rect_dict = {'id': 89, 'width': 10, 'height': 4}
        rect = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.to_dictionary(), rect_dict)

        square_dict = {'id': 90, 'size': 5}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.to_dictionary(), square_dict)

    def test_save_to_file(self):
        """
        Tests the `save_to_file` class method.
        """
        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        # Add code to verify the contents of the file here

    def test_load_from_file(self):
        """
        Tests the `load_from_file` class method.
        """
        # Create and save some Rectangles and Squares
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4)
        Rectangle.save_to_file([rect1, rect2])

        square1 = Square(5)
        square2 = Square(7, 9, 1)
        Square.save_to_file([square1, square2])

        # Load them from file
        rects = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertTrue(all(isinstance(obj, Rectangle) for obj in rects))
        self.assertTrue(all(isinstance(obj, Square) for obj in squares))

        # Add more specific tests to compare the properties of loaded objects
        # with those of the original objects

    # Add more tests for any other methods in the Base class you wish to test

if __name__ == "__main__":
    unittest.main()

