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
    def t