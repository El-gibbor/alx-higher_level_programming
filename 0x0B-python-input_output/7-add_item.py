#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file:"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


av = argv[1:]
filename = 'add_item.json'
try:
    item = load_from_json_file(filename)
except FileNotFoundError:
    item = []
item += av
save_to_json_file(item, filename)
