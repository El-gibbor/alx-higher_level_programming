#!/usr/bin/python3
"""a class module"""


class Node:
    """defining the node"""
    
    def __init__(self, data, next_node=None):
        """initialising object attributes

        Args:
            data (int): value/content of each node
            next_node (Node): next node in the l-list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node
        
    @property
    def data(self):
        """retrieve/return the data attribute"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """check, validate and set the value for data

        Args:
            value (int): value/content of each node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        
    @property
    def next_node(self):
        """retrieve/return next node attribute"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """check, validate and set next node attribute

        Args:
            value (int): next node in the l-list
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """defines a singly linked list"""
    
    def __init__(self):
        """initialise an empty singly linked list"""
        self.__head = None
        
    def __str__(self):
        """human-readble reprensation of the singly l-list"""
        node = ""
        l_node = self.__head # assign an iterator to head to loop through the l-list
        while l_node:
            # each node data seperated by newline asper alx demand
            node += str(l_node.data) + "\n"
            l_node = l_node.next_node
        return node[:-1] # ([:-1]) -> exempts a "\n" at the end
    
        """using list comprehension (optional)"""
    # def __str__(self):
    #       return '\n'.join(str(n.data) for n in self)
    
    def sorted_insert(self, value):
        """inserts Nodes in a sorted manner (increasing order)"""
        new_node = Node(value)
        node = self.__head
        if node is None or node.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        while node.next_node is not None and node.next_node.data < new_node.data:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
