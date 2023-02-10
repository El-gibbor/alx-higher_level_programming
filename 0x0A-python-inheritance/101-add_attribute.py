#!/usr/bin/python3
"""module that adds attribute to a given object"""


def add_attribute(object, attribute, value):
    """_summary_

    Args:
        object (class): object where the new attribute is added
        attribute (str): name of attribute/property to be added
        value (str): value to be added. eg: value of age, name etc

    Raises:
        TypeError: if the object's __dic__ attr doesn't have a writable attr
    """

    if hasattr(object, "__dict__"):
        setattr(object, attribute, value)
    else:
        raise TypeError("can't add new attribute")
