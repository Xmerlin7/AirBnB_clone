#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel


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
        """
        Adds a new object to the __objects dictionary.
        """
        ObjName = obj.__class__.__name__
        key = "{}.{}".format(ObjName, obj.id)
        FileStorage.__objects[key] = obj 

    def save(self):
        """
        Serializes the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        all_obj = FileStorage.__objects
        obj_dict = {}
        for key, value in all_obj.items():
            obj_dict[key] = value.to_dict()  # Correctly calling the to_dict method
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)  # Writing the dictionary to a JSON file

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name = key.split('.')[0]
                        id = key.split('.')[1]
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects = instance
                    # for key, value in obj_dict.items():
                    #     class_name, obj_id = key.split('.')

                    #     cls = eval(class_name)

                    #     instance = cls(**value)

                    #     FileStorage.__objects[key] = instance                    
                except FileNotFoundError:
                    pass