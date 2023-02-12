#!/usr/bin/python3

import unittest
import datetime
import json
import os
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ Set up method run before each test cases. """
        pass

    def tearDown(self):
        """ Tear down method run after each test cases. """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test if the instance is of the correct type. """
        i = BaseModel()
        self.assertIsInstance(i, BaseModel)

    def test_kwargs(self):
        """ Test if the instance created from kwargs is not the same object as the original. """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertIsNot(new, i)

    def test_kwargs_int(self):
        """ Test if passing an int as a kwarg raises TypeError. """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Test if the instance is saved to file. """
        i = BaseModel()
        i.save()
        key = "BaseModel." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Test if the string representation of the instance is correct. """
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

    def test_to_dict(self):
        """ Test if the to_dict method returns the correct dictionary. """
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test if passing None as a kwarg raises TypeError. """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """ Test if passing a single kwarg raises KeyError. """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """ Test if the instance has a correct id. """
        new = BaseModel()
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """ Test if the instance has a correct created_at value. """
        new = BaseModel()
        self.assertIsInstance(new.created_at, datetime.datetime)

    def test_updated_at(self):
        """ Test the type and correctness of the `updated_at` attribute """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
