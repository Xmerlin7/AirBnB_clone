#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary. 
        It provides access to all the stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        ObjName = obj.__class__.__name__
        key = "{}.{}".format(ObjName, obj.id)
        FileStorage.__objects[key] = obj 

    def save(self):
        

    def reload(self):
        pass

    