#!/usr/bin/python3
"""This module defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    
    def __init__(self, *args, **kwargs):
        """Defines all common attributes/methods for other classes"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            #self.storage.new(self)
    
    
    def __str__(self):
        """Returns a string for the basemodel instance"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
    def save(self):
        pass
    def to_dict(self):
        pass