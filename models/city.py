#!/usr/bin/python3
""" Project 0x00. AirBnB clone - The console
    Task 10
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class
    """
    state_id = ""
    name = ""

    def __init__(self):
        """Initializes state id and name
        """
        pass
