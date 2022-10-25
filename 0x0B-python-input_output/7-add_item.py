#!/usr/bin/python3
"""
Module 7-add_item

Script that adds all arguments to a Python list, and then saves them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filemane = "add_item.json"
json_list = []
try:
    json_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(json_list, filename)

arg_len = len(argv)
if arg_len > 1:
    for i in range(1, arg_len):
        json_list.append(i)

    save_to_json_file(json_list, filename)
