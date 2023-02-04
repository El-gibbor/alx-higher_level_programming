#!/usr/bin/python3
"""a module that defines a square of # character"""


class Square:
    """defines a square"""
    
    def __init__(self, size=0, position=(0, 0)):
        """initializing the instance attributes"""
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """retrieve/return the instance attribute size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """check, validate andf set value for instance attr, size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=o")
        self.__size = value
        
    @property
    def position(self):
        """retrieve/return the instance attribute position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """check, validate andf set value for instance attr, position."""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
    
    def area(self):
        """returns the current square area"""
        return self.__size ** 2
    
    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size is 0:
            print()
        for i in range(self.__size):
            space = " " * self.__position[0]
            hash = "#" * self.__size
            print(space + hash)

        for i in range(self.__position[1]):
            print("")
            
    def __str__(self):
        return f'Square of size: {self.__size} and position: {self.__position}'
