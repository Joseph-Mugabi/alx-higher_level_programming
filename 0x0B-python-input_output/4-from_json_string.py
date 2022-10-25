#!/usr/bin/python3
"""
module 4-from_json_string

Contains the "to_json_string" fundtion
"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented
    by a JSON string"""
    return json.loads(my_str)
