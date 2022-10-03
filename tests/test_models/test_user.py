#!/usr/bin/python3
"""
test_user is a module used for unit testing of 
the User class.
"""
import unittest
from models.user import User as User



class UserTests(unittest.TestCase):
    """
    Class UserTests provides unit testing for
    the User class.
    """
    @classmethod
    def setUp(cls):
        """
        Method to set up BaseModel classes for use during testing.
        """
        cls.user1 = User()
        cls.user2 = User()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down BaseModel classes for use during testing.
        """
        del cls.user1
        del cls.user2
        return super().tearDownClass()

    def test_class_attrs(self):
        self.assertEqual(self.user1.email, "")
        self.assertEqual(self.user1.password, "")
        self.assertEqual(self.user1.first_name, "")
        self.assertEqual(self.user1.last_name, "")
        self.assertIsInstance(self.user1.email, str)
        self.assertIsInstance(self.user1.password, str)
        self.assertIsInstance(self.user1.first_name, str)
        self.assertIsInstance(self.user1.last_name, str)


if __name__ == '__name__':
    unittest.main()
