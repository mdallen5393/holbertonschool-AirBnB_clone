#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """ State class
    """
    def __init__(self):
        """Initializes Name of state
        """
        self.state = ""
