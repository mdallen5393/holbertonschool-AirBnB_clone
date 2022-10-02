#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """ City class
    """
    def __init__(self):
        """Initializes state id and name
        """
        self.state_id = ""
        self.name = ""
