# pylint: disable=too-many-instance-attributes
#!/usr/bin/python3
"""a module that contains a sub class from class, Base """

from models.base import Base


class Rectangle(Base):
    """initializes instance attributes"""

    # pylint: ignored=too-many-instance-attributes
    # i have only 5 which is not even upto 7

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all attributes of rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate axis of rectangle
            y (int): y-coordinate axis of rectangle

            Note:
                x and y cordinate of a rectangle can be zero, This is because
                The origin, which is represented by the point(0,0), is where
                x & y axes intersect. so, the setter properties for x & y value
                validates if they're less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # inherites the base class attr logic
        super().__init__(id)

    @property
    def width(self):
        """retrieves the private attr of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the private attr of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the private attr of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the private attr of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints the rctangle shape with # """
        for _ in range(self.y):
            print("")
        for _ in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """# triangle character taking x and y corndinates into account"""
        for _ in range(self.y):
            print("")
        for _ in range(self.__height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """updates/assign an argument to each attribute. the else clause
        ensures that the attribute retains its original, previous or default
        value of optional argument when no argument is provided for update
        in this method()
        """
        self.id = args[0] if len(args) >= 1 else self.id
        self.width = args[1] if len(args) >= 2 else self.width
        self.height = args[2] if len(args) >= 3 else self.height
        self.x = args[3] if len(args) >= 4 else self.x
        self.y = args[4] if len(args) >= 5 else self.y

    # def update(self, *args, **kwargs):
    #     """unpacks the key-value paired key word arguments to update
    #     the attributea. happens only when *args doesnt exit or empty
    #     """
    #     if len(args) > 0:
    #         self.id, self.width, self.height, self.x, self.y = args
    #     else:
    #         for keyz, valz in kwargs.items():
    #             setattr(self, keyz, valz)
