#!/usr/bin/python3
"""
class module Base
"""

import json
import csv


class Base():
    """
    defines class Base
    private class attributes:
        __nb_objects
    methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing id, increment class attribute if no id and set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objects = []
        if list_objs is not None:
            for objs in list_objs:
                objects.append(cls.to_dictionary(objs))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        load = []
        try:
            with open(filename, "r") as f:
                load = cls.from_json_string(f.read())
            for idx, dic in enumerate(load):
                load[idx] = (cls.create(**load[idx]))
        except IOError:
            pass
        return load

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                    obj.x, obj.y])
                if cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ """
        obj = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for r in reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {"id": int(r[0]), "width": int(r[1]),
                                  "height": int(r[2]), "x": int(r[3]),
                                  "y": int(r[4])}
                if cls.__name__ == "Square":
                    dictionary = {"id": int(r[0]), "size": int(r[1]),
                                  "x": int(r[2]), "y": int(r[3])}
                objs = cls.create(**dictionary)
                obj.append(objs)
        return obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for idx in list_rectangles + list_squars:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((idx.x + t.pos()[0], ind.y - t.pos()[1]))
            t.pensize(10)
            t.forward(idx.width)
            t.left(90)
            t.forward(idx.height)
            t.left(90)
            t.forward(idx.width)
            t.left(90)
            t.forward(idx.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
