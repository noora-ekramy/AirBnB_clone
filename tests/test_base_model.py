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

    def test_save_method_updates_updated_at(self):
        model = BaseModel()
        first_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(first_updated_at, model.updated_at)

    def test_to_dict_returns_correct_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('__class__', model_dict)

    
    def test_id_is_unique(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_str_representation(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(expected_str, str(model))


if __name__ == '__main__':
    unittest.main()

