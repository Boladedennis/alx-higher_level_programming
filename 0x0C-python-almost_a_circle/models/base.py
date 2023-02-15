#!/usr/bin/python3
"""
Intialize a class named base
"""
import json
import csv



class Base():
    """
    Definition of class base 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation to list_objs to file"""
        fname = cls.__name__+ ".json"
        lista = []
        with open(fname, mode='w', encoding='utf-8') as a_file:
            if list_objs is None:
                a_file.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    lista.append(obj.to_dictionary())
                a_file.write(cls.to_json_string(lista))
