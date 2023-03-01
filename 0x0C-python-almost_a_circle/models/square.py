 #!/usr/bin/python3
"""a module for square which inherites the Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing attr by using the __init__ logic of the superclass"""
        super().__init__(size, size, x, y, id)
        self.size = size

        """p-decorator for size attribute. this sets the value for both
        height and width, ensuring the value of height and width are
        always equal for a square object.
        """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size_val):
        """validations are already implemented in the superclass
        property decorator & setter
        """
        self.width = size_val
        self.height = size_val

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """info about this method() is documented in the superclass
        update method()
        """
        self.id = args[0] if len(args) >= 1 else self.id
        self.size = args[1] if len(args) >= 2 else self.size
        self.x = args[2] if len(args) >= 3 else self.x
        self.y = args[3] if len(args) >= 4 else self.y

        for keyz, valz in kwargs.items():
            setattr(self, keyz, valz)

    def to_dictionary(self):
        """returns dictionary representation of rectangle (it's attributes)"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
