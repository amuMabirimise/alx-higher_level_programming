#!/usr/bin/python3
'''
a models with an empty file

'''

import json
import csv


class Base:
    '''
    represents the Base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor representation
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        dictionary representation
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns list of JSON
        '''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves JSON directory
        '''
        listdict = []
        if not list_objs:
            list_objs = []
        for items in list_objs:
            listdict.append(items.to_dictionary())

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(listdict))

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns instance set
        '''
        if cls.__name__ is 'Rectangle':
            newInstance = cls(1, 1)
            newInstance.update(**dictionary)
            return newInstance
        if cls.__name__ is 'Square':
            newInstance = cls(1)
            newInstance.update(**dictionary)
            return newInstance
        else:
            return None

    @classmethod
    def load_from_file(cls):
        '''
        Returns instances
        '''
        instanceList = []
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            instanceList.append(cls.create(**dictionary))
        return instanceList

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        csv
        '''
        listToDictionary = []
        if list_objs is not None:
            list_objs = []
        for items in list_objs:
            listToDictionary.append(items.to_dictionary())

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''
        list
        of instances
        '''
        instanceList = []
        try:
            with open('{}'.format(cls.__name__), 'r', encoding='utf-8') as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            instanceList.append(cls.create(**dictionary))
        return instanceList
