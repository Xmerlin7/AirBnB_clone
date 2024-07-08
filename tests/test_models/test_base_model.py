import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Uint testing for BaseMdoel Class
    """
    def test_init(self):
        """
        Test for init constructor
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        base_model = BaseModel()
        self.assertNotEqual(base_model.save(), base_model.updated_at)

    def test_dict(self):
        base_model = BaseModel()
        base_model_dict = BaseModel.to_dict()
        self.assertIsInstance(base_model, base_model_dict)
        self

    