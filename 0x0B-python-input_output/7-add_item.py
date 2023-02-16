#!/usr/bin/python3
"""
This module contains a script that adds all cmd-line args to a python list,
and save them to a json file
"""

from sys import argv

if __name__ == "__main__":

    save_to_json = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file =\
        __import__("6-load_from_json_file").load_from_json_file

    try:
        arg_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_list = []
    arg_list.extend(argv[1:])
    save_to_json(arg_list, "add_item.json")
