#!/usr/bin/python3
import json
import csv
import turtle
'''Base class module'''


class Base:
    '''declaration of class'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''constructor of class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method that returns Json format'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        '''write Json serialization to file'''
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            
            else:
                list_json = [listed.to_dictionary() for listed in list_objs]
                file.write(Base.to_json_string(list_json))
    
    @staticmethod
    def from_json_string(json_string):
        '''static method that deserialize json file'''
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        '''return a class instance from dictionary of attributes'''
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new = cls(1,1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    
    @classmethod
    def load_from_file(cls):
        '''Return list of classes inherited from file'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''function that saves to CSV file'''
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline="") as csv_file:
            if list_objs is None or list_objs == []:
                return csv_file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = [
                        'id','width','height','x','y'
                    ]
                else:
                    fieldnames = ['id','size','x','y']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for lines in list_objs:
                    writer.writerow(lines.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

            