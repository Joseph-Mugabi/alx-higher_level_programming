#!/usr/bin/python3
"""
unittests for class Base
# python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest, json
import sys, os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO


class Test_Base_Class(unittest.TestCase):
    """tests the base class"""
    
    def setUp(self):
        """initializes, instantiates class"""
        Base._base__nb_objects = 0
        pass

    def tearDown(self):
        """cleans up after each test_method"""
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_class(self):
        """tests whether the class created is a Base"""
        self.assertTrue(Base(100), self.__class__ == Base)

    def test_many_args_error(self):
        """test whether too many arguments given error raises"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_nb_objects_private(self):
        """tests if the nb_objects is private class attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_nb_objects_init(self):
        """tests nb_objects initializes to 0"""
        self.assertTrue(getattr(Base, "_Base__nb_objects"), 0)

    def test_id_given(self):
        """test if ids match when given"""
        self.assertTrue(Base(-89), self.id == -89)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(999), self.id == 999)

    def test_id_not_given(self):
        """test ids match incremented nb_objects when not given"""
        self.assertTrue(Base(), self.id == 0)
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_from_none_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty dict"""
        d3 = dict()
        strd3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3, "[]")

    def test_from_json_string(self):
        """Test JSON string translates into Python dict"""
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
                {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
            [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs0[0],
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_empty_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

    def test_save_to_file(self):
        """Test save to file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r.to_dictionary(),
                r2.to_dictionary()]), file.read())

    def test_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_none_file(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

if __name__ == '__main__':
        unittest.main()
