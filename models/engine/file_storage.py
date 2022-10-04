#!/usr/bin/python3
"""
file_storage module that contains the FileStorage class
definition and methods
"""
from models.base_model import BaseModel
import json
import os
import models
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """
    FileStorage class which serializes instances to a JSON file
    and deserializes JSON files to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary `__objects`.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key `<obj class name>.id`.
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file.
        """
        ObjectDict = {}
        for key, value in self.__objects.items():
            ObjectDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf=8') as f:
            f.write(json.dumps(ObjectDict))

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                LoadDict = json.loads(f.read())
            for key, val in LoadDict.items():
                self.__objects[key] = eval(val["__class__"])(**val)
