#!/usr/bin/python3
"""Test cases for console.py"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import *
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State name=\"California\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if UUID is printed

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            create_command = "create State name=\"California\""
            show_command = "show State {}".format(self.console.onecmd(create_command).strip())
            self.console.onecmd(show_command)
            output = mock_stdout.getvalue().strip()
            self.assertTrue("California" in output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            state_id = self.console.onecmd("create State name=\"California\"").strip()
            destroy_command = "destroy State {}".format(state_id)
            self.console.onecmd(destroy_command)
            show_command = "show State {}".format(state_id)
            self.console.onecmd(show_command)
            output = mock_stdout.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State name=\"California\"")
            self.console.onecmd("create State name=\"New York\"")
            self.console.onecmd("all State")
            output = mock_stdout.getvalue().strip()
            self.assertTrue("California" in output)
            self.assertTrue("New York" in output)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            state_id = self.console.onecmd("create State name=\"California\"").strip()
            update_command = "update State {} name \"New California\"".format(state_id)
            self.console.onecmd(update_command)
            show_command = "show State {}".format(state_id)
            self.console.onecmd(show_command)
            output = mock_stdout.getvalue().strip()
            self.assertTrue("New California" in output)


if __name__ == '__main__':
    unittest.main()
