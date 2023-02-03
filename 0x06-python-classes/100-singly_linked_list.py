#!/usr/bin/python3
"""a class, Node"""


class Node:
    """defines a Node"""

    def __init__(self, data, next_node=None):
        """initialize instance attributes, propereties of the list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve/return data for each node"""
        return self.__data

    @data.setter
    def data(self, value):
        """check, validate and set the value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retreive/return the value of Next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """check, validate and set the value of next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        """creating structure of the linked list"""
        self.__head = None

    def __str__(self):
        """display the contents of linkedl list"""
        node_ = ""
        # asign an iterator to head and treverse the entire l-list
        n = self.__head
        while n:
            # print & seperate each data of node with a newline
            node_ += str(n.data) + "\n"
            n = n.next_node
        return (node_[:-1])
    
    def sorted_insert(self, value):
        """inserts a new node into the correct increasing sorted order"""
        new_node = Node(data) # initialise the node with data/value
        if self.__head is None:
            self.__head = new_node
            return
        # insert node at begining if the data is smaller than data where head points to
        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_n = self.__head
            while current_n.next_node and new_node.data > current_n.next_node.data:
                current_n = current_n.next_node
                new_node.next = current_n.next_node
                current_n.next_node = new_node
