#!/usr/bin/python3
"""
file_storage module that contains the FileStorage class
definition and methods
"""


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
        pass

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        pass