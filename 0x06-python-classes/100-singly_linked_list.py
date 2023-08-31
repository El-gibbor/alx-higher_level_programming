#!/usr/bin/python3
""" a class Node that defines a node of a singly linked list"""


class Node:
    """class definition"""

    def __init__(self, data, next_node=None):
        """
            Instantiates a node object for the singly linked list
        Args:
            data (int) - value in the node
            next_node - reference/pointer to the next node
        """
        self.data = data
        self.next_node = next_node

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
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """instantiate head for the linked list"""
        self.head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct sorted position """

        new_node = Node(value)  # creates a node object with its data
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        curr = self.head
        while curr.next_node and curr.next_node.data < value:
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node

    def __str__(self):
        """print entire list to stdout, one node number by line"""

        dummy_list, to_stdout = self.head, []

        while dummy_list:
            to_stdout.append(str(dummy_list.data))
            dummy_list = dummy_list.next_node
        return '\n'.join(to_stdout)
