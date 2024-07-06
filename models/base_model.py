#!/usr/bin/python3
"""This module defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
    
    def __init__(self, *args, **kwargs):
        """Defines all common attributes/methods for other classes"""
        
    
    
    def __str__(self):
        pass
    def save(self):
        pass
    def to_dict(self):
        pass