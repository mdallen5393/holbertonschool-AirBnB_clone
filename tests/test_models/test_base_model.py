#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel as BaseModel
import pathlib


class BaseModelTests(unittest.TestCase):
    """
    Class BaseModelTests that provides unit testing for the
    `BaseModel` class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Method to set up BaseModel classes for use during testing.
        """
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """
        Method to tear down BaseModel classes for use during testing.
        """
        del cls.base1
        del cls.base2
        return super().tearDownClass()

    def test_init(self):
        """
        Method for testing initialization of the BaseModel class.
        """
        self.assertIsNotNone(self.base1)
        self.assertIsNotNone(self.base1.id)
        self.assertIsInstance(self.base1, BaseModel)
        self.assertNotEqual(self.base1.id, self.base2.id)
        test_dict = self.base1.to_dict()
        base3 = BaseModel(test_dict)
        self.assertNotEqual(self.base1, base3)
        self.assertNotEqual(self.base1.id, base3.id)
        self.assertIsInstance(test_dict['created_at'], str)
        self.assertIsInstance(test_dict['updated_at'], str)
        del base3

    def test_datetimes(self):
        """
        Method for testing datetime attributes
        """
        testdt = datetime.now()
        self.assertEqual(self.base1.created_at.year, testdt.year)
        self.assertEqual(self.base1.created_at.month, testdt.month)
        self.assertEqual(self.base1.created_at.day, testdt.day)
        self.assertEqual(self.base1.created_at.hour, testdt.hour)
        self.assertEqual(self.base1.created_at.minute, testdt.minute)
        self.assertEqual(self.base1.created_at.second, testdt.second)
        self.assertEqual(self.base1.updated_at.year, testdt.year)
        self.assertEqual(self.base1.updated_at.month, testdt.month)
        self.assertEqual(self.base1.updated_at.day, testdt.day)
        self.assertEqual(self.base1.updated_at.hour, testdt.hour)
        self.assertEqual(self.base1.updated_at.minute, testdt.minute)
        self.assertEqual(self.base1.updated_at.second, testdt.second)

    def test_str(self):
        """
        Method to test __str__ function of a BaseModel.
        """
        test_str = f"[{type(self.base1).__name__}] \
({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(str(self.base1), test_str)

    def test_save(self):
        """
        Method to test save function of a BaseModel
        """
        self.base1.save()
        testdt = datetime.now()
        self.assertEqual(self.base1.created_at.year, testdt.year)
        self.assertEqual(self.base1.created_at.month, testdt.month)
        self.assertEqual(self.base1.created_at.day, testdt.day)
        self.assertEqual(self.base1.created_at.hour, testdt.hour)
        self.assertEqual(self.base1.created_at.minute, testdt.minute)
        self.assertEqual(self.base1.updated_at.year, testdt.year)
        self.assertEqual(self.base1.updated_at.month, testdt.month)
        self.assertEqual(self.base1.updated_at.day, testdt.day)
        self.assertEqual(self.base1.updated_at.hour, testdt.hour)
        self.assertEqual(self.base1.updated_at.minute, testdt.minute)
        self.assertEqual(self.base1.updated_at.second, testdt.second)
        path = pathlib.Path("file.json")
        self.assertTrue(path.is_file())
        with open("file.json", 'r', encoding='utf-8') as f:
            json_str = f.read()
            self.assertIsNotNone(json_str)
        self.assertIn(f"{self.base1.__class__.__name__}.{self.base1.id}", json_str)

    def test_to_dict(self):
        """
        Method to test to_dict function of a BaseModel
        """
        test_dict = self.base1.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict['id'], self.base1.id)
        create_iso = self.base1.created_at.isoformat()
        update_iso = self.base1.updated_at.isoformat()
        self.assertEqual(test_dict['created_at'], create_iso)
        self.assertEqual(test_dict['updated_at'], update_iso)
        self.assertIn('__class__', test_dict)


if __name__ == '__name__':
    unittest.main()
