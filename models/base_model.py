#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializer for BaseModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()  # TODO: possibly needs to be moved

    def __str__(self):
        """
        Returns a string representation of a BaseModel
        instance.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        `__dict__` of the instance.
        """
        myDict = self.__dict__.copy()
        myDict['__class__'] = type(self).__name__
        myDict['created_at'] = self.created_at.isoformat()
        myDict['updated_at'] = self.created_at.isoformat()
        return myDict

