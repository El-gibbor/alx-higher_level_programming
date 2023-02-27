#!/usr/bin/python3
"""a module for square which inherites the Rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """defines a Square"""
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
    