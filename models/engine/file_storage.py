#!/usr/bin/python3
"""
file_storage module that contains the FileStorage class
definition and methods
"""
from models.base_model import BaseModel
import json
import os
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
    def __init__(self):
        """
        Initializer for FileStorage objects.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary `__objects`.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key `<obj class name>.id`.
        """
        key = f'{type(obj).__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file.
        """
        ObjectDict = {}
        for key in self.__objects:
            ObjectDict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(ObjectDict, f)

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                LoadDict = json.load(f)
            self.__objects.update(LoadDict)
