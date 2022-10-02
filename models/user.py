#!/usr/bin/python3
""" Project 0x00. AirBnB clone - The console
    Task 9
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
    """
    def __init__(self):
        """ initializing public user attributes
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
