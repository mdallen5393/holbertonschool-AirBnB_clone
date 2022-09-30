#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""
import unittest
from models.base_model import BaseModel as BaseModel

class BaseModelTests(unittest.TestCase):
    """
    Class BaseModelTests that provides unit testing for the
    `BaseModel` class.
    """
    # @classmethod
    # def setUpClass(cls) -> None:
    #     return super().setUpClass()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     return super().tearDownClass()

    def test_init(self):
        """
        Method for testing initialization of the BaseModel class.
        """
        new = BaseModel()
        self.assertIsNotNone(new)