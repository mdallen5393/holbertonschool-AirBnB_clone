#!/usr/bin/python3
"""
Unittest module for FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage as FileStorage
from models.base_model import BaseModel as BaseModel


class FileStorageTests(unittest.TestCase):
    """
    Class FileStorageTests that provides unit testing for the
    `FileStorage` class.
    """
    def setUp(cls):
        """
        Method to set up FileStorage classes for use during testing.
        """
        cls.fs1 = FileStorage()
        cls.fs2 = FileStorage()
        cls.bm1 = BaseModel()

    def tearDown(cls):
        """
        Method to tear down FileStorage classes for use during testing.
        """
        del cls.fs1
        del cls.fs2
        del cls.bm1
        return super().tearDown()

    def test_init(self):
        """
        Method for testing initialization of the FileStorage class.
        """
        self.assertIsNotNone(self.fs1)
        self.assertIsInstance(self.fs1, FileStorage)
        self.assertIsNotNone(self.fs1._FileStorage__file_path)
        self.assertEqual(self.fs1._FileStorage__file_path, "file.json")
        self.assertIsNotNone(self.fs1._FileStorage__objects)
        self.assertIsInstance(self.fs1._FileStorage__objects, dict)

    def test_all(self):
        """
        Method for testing functionality of the all() method
        of the FileStorage class.
        """
        self.assertIsNotNone(self.fs1.all())
        self.assertIsInstance(self.fs1.all(), dict)
        self.fs1.new(self.bm1)
        key = f'BaseModel.{self.bm1.id}'
        self.assertIsNotNone(self.fs1.all(), {key: self.bm1})

    def test_new(self):
        """
        Method for testing functionality of the new() method
        of the FileStorage class.
        """
        pass

    def test_save(self):
        """
        Method for testing functionality of the save() method
        of the FileStorage class.
        """
        pass # FIXME:

    def test_reload(self):
        """
        Method for testing functionality of the reload() method
        of the FileStorage class.
        """
        pass # FIXME:


if __name__ == '__name__':
    unittest.main()
