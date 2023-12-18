#!/usr/bin/python3
"""base model test module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_id_creation(self):
        """Test that id is created correctly"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_updated_at(self):
        """Test creation and update timestamps"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

if __name__ == '__main__':
    unittest.main()

