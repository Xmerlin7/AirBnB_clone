import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit testing for BaseModel Class
    """

    def test_init(self):
        """
        Test for init constructor
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str(self):
        """
        Test for str method
        """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

    def test_save(self):
        """
        Test for save method
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
