#!/usr/bin/python3
""" Project 0x00. AirBnB clone - The console
    Task 10
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class
    """
    place_id = ""
    user_id = ""
    text = ""
