#!/usr/bin/python3
"""
Intializing a class
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle that intiaties from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > than 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ gette for y """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """
        area attribute
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle instance
        """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ string method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}". format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ assign argument to each attriute """
        attrs = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) !=0:
            for i in range(len(args)):
                if i >= len(attrs):
                    break
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """adding public method dictionary"""
        attrs = ["id", "width", "height", "x", "y"]
        values = [self.id, self.width, self.x, self.y]
        return dict(zip(attrs, values))
