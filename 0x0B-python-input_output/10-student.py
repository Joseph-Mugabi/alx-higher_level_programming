#!/usr/bin/python3
"""
Module 10-student

Contains the clas "Student"
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for at in attrs:
                if at in self.__dict__.key():
                    new_dict[at] = self.__dict__[at]
        return new_dict
