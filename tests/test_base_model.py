#!/usr/bin/python3
""" Unit tests for the BaseModel class. """

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
import os
import json
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """ Defines a class to test BaseModel features. """

    @classmethod
    def setUpClass(cls):
        """ Set up resources before any test methods. """
        cls.storage_backup = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """ Clean up resources after all test methods. """
        FileStorage._FileStorage__objects = cls.storage_backup

    def setUp(self):
        """ Set up before each test method. """
        self.test_model = BaseModel()
    
    def tearDown(self):
        """ Clean up after each test method. """
        del self.test_model

    def test_initialization(self):
        """ Test initialization of BaseModel. """
        self.assertIsInstance(self.test_model, BaseModel)
        self.assertIsInstance(self.test_model.id, str)
        self.assertIsInstance(self.test_model.created_at, datetime)
        self.assertIsInstance(self.test_model.updated_at, datetime)

    def test_initialization_with_kwargs(self):
        """ Test initialization with kwargs. """
        test_id = str(uuid.uuid4())
        model_with_kwargs = BaseModel(id=test_id, name="Test Model")
        self.assertEqual(model_with_kwargs.id, test_id)
        self.assertEqual(model_with_kwargs.name, "Test Model")

    def test_to_dict(self):
        """ Test conversion to dictionary. """
        model_dict = self.test_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_save(self):
        """ Test save method of BaseModel. """
        old_updated_at = self.test_model.updated_at
        time.sleep(0.1)
        self.test_model.save()
        new_updated_at = self.test_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_str(self):
        """ Test string representation of BaseModel. """
        expected_str = f"[BaseModel] ({self.test_model.id}) {self.test_model.__dict__}"
        self.assertEqual(str(self.test_model), expected_str)

if __name__ == "__main__":
    unittest.main()


