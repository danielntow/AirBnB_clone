import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            self.console.onecmd(f"count BaseModel")
            output_lines = mock_stdout.getvalue().strip().split('\n')
            self.assertEqual(len(output_lines), 2)
            storage.save()

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIsNotNone(output)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)


if __name__ == '__main__':
    unittest.main()
