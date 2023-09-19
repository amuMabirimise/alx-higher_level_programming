#!/usr/bin/python3
'''
defines a class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        init Constructor
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        size setter getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        size setter
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        variadic arg
        '''
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except BaseException:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''
       Pull the parameters out in

        '''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def __str__(self):
        '''
        String representation of str
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.size)
