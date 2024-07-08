#!/usr/bin/python3
"""This module defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models
# from models import storage

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
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
            # storage.new(self)
    
    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        obj = self.__dict__.copy()
        obj["__class__"] = self.__class__.__name__
        obj["created_at"] = self.created_at.isoformat()
        obj["updated_at"] = self.updated_at.isoformat()
        return obj

