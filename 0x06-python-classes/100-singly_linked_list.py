#!/usr/bin/python3
""" a class Node that defines a node of a singly linked list"""


class Node:
    """class definition"""

    def __init__(self, data, next_node=None):
        """
            Instatiates a node of a singly linked list
        Args:
            data (int) - value in the node
            next_node - reference/pointer to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves the data attribte of Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """validates and set the data value of node"""

        if type(value) is not int:
            raise Exception('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrives reference of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """validate and sets reference to the next node"""
        if

class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""

