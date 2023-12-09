#!/usr/bin/python3
"""base model test module"""
import datetime
import unittest
from models.base_model import BaseModel


class testBaseModel_init(unittest.TestCase):
    """class for testing of base model instantiation"""
    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)




if __name__ == "__main__":
    unittest.main()
