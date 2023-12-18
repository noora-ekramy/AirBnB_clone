#!/usr/bin/python3

""" Unit tests for the file_storage class. """
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.key = f"{type(self.model).__name__}.{self.model.id}"

    def tearDown(self):
        """ Clean up after tests """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """ Test that all returns the correct dictionary """
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(self.key, self.storage.all())

    def test_new(self):
        """ Test that new correctly adds an object """
        self.storage.new(self.model)
        self.assertIn(self.key, self.storage.all())

    def test_save(self):
        """ Test that save correctly writes to the file """
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """ Test that reload correctly reads from the file """
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(self.key, self.storage.all())

if __name__ == '__main__':
    unittest.main()