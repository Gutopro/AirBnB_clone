#!/usr/bin/python3

"""
    Unittest for base_model.py
"""
import datetime
import unittest
import sys

# add two directories back to the sys.path list
sys.path.append("..")
sys.path.append("..")

from models.Basemodel import BaseModel


class TestDatetimeISOFormat(unittest.TestCase):
    def test_to_dict_method(self):
        """Test the to_dict method of the BaseModel class."""
        dt = datetime.now()
        bm = BaseModel(created_at=dt, updated_at=dt)
        expected_output = bm.created_at.isoformat()
        self.assertEqual(bm.to_dict()["created_at"], expected_output)

if __name__ == '__main__':
    unittest.main()
