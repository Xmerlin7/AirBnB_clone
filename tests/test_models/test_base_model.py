import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Uint testing for BaseMdoel Class
    """
    def test_init(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        
    def test_save(self):
        
        