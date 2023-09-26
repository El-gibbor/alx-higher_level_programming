#!/usr/bin/python3
""" Class to json """


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return vars(obj) #  same as self.__dict__
