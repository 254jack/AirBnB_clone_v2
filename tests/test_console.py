#!/usr/bin/python3
"""Test cases for console.py"""
import unittest
import os
from models import storage
from console import HBNBCommand
from models.base_model import *
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State


class TestConsoleCreateCommand(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.console.classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State,
                                'City': City, 'Amenity': Amenity, 'Review': Review}
        self.file_path = "file.json"

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_create_instance(self):
        """Test creating an instance using the create command"""
        self.console.onecmd("create BaseModel name=\"TestObject\"")
        object_id = self.console.onecmd("all BaseModel")
        print("object_id:", object_id)  # Debugging statement
        obj = storage.all().get(object_id.strip('[]').split()[0])
        print("obj:", obj)  # Debugging statement
        self.assertEqual(obj.name, "TestObject")

    def test_create_instance_float(self):
        """Test creating an instance with float value"""
        self.console.onecmd("create BaseModel float_value=3.14")
        object_id = self.console.onecmd("all BaseModel")
        print("object_id:", object_id)  # Debugging statement
        obj = storage.all().get(object_id.strip('[]').split()[0])
        print("obj:", obj)  # Debugging statement
        self.assertEqual(obj.float_value, 3.14)

    def test_create_instance_integer(self):
        """Test creating an instance with integer value"""
        self.console.onecmd("create BaseModel int_value=42")
        object_id = self.console.onecmd("all BaseModel")
        print("object_id:", object_id)  # Debugging statement
        obj = storage.all().get(object_id.strip('[]').split()[0])
        print("obj:", obj)  # Debugging statement
        self.assertEqual(obj.int_value, 42)

    def test_create_instance_invalid_params(self):
        """Test creating an instance with invalid parameters"""
        self.console.onecmd("create BaseModel invalid_param=invalid_value")
        object_id = self.console.onecmd("all BaseModel")
        print("object_id:", object_id)  # Debugging statement
        self.assertEqual(object_id.strip('[]').split(), [])

if __name__ == '__main__':
    unittest.main()
