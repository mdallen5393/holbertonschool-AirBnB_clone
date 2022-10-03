#!/usr/bin/python3
""" Project 0x00. AirBnB clone - The console
    Task 9
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
