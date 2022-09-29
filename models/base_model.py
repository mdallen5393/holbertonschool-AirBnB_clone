#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self):
        """
        Initializer for BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """
        Returns a string representation of a BaseModel
        instance.
        """
        pass

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.
        """
        pass

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        `__dict__` of the instance.
        """
        pass
