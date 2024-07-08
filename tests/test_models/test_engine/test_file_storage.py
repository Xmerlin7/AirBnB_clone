#!/usr/bin/python3
"""
Module for testing and deserializing data
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage.__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        my_base_model = BaseModel()
        models.storage.new(my_base_model)
        self.assertIn("BaseModel." + my_base_model.id, models.storage.all().keys())


if __name__ == "__main__":
    unittest.main()