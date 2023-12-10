from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
import os


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


"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommandPrompting
    TestHBNBCommandHelp
    TestHBNBCommandExit
    TestHBNBCommandCreate
    TestHBNBCommandShow
    TestHBNBCommandAll
    TestHBNBCommandDestroy
    TestHBNBCommandUpdate
"""


class TestHBNBCommandPrompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        expected_output = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected_output, output.getvalue().strip())

    # ... (similar modifications for other help tests)

    def test_help(self):
        expected_output = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  count  create  destroy  help  quit  show  update"
        )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected_output, output.getvalue().strip())


class TestHBNBCommandExit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommandCreate(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self):
        class_names = ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]
        for class_name in class_names:
            with self.subTest(class_name=class_name):
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(
                        f"create {class_name}"))
                    self.assertGreater(len(output.getvalue().strip()), 0)
                    test_key = f"{class_name}.{output.getvalue().strip()}"
                    self.assertIn(test_key, storage.all().keys())


class TestHBNBCommandShow(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id(self):
        correct = "** instance id missing **"
        test_commands = ["show BaseModel", "show User", "show State",
                         "show City", "show Amenity", "show Place", "show Review"]
        for command in test_commands:
            with self.subTest(command=command):
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found(self):
        correct = "** no instance found **"
        test_commands = ["show BaseModel 1", "show User 1", "show State 1",
                         "show City 1", "show Amenity 1", "show Place 1", "show Review 1"]
        for command in test_commands:
            with self.subTest(command=command):
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(correct, output.getvalue().strip())

    def test_show_objects(self):
        class_names = ["BaseModel", "User", "State",
                       "Place", "City", "Amenity", "Review"]
        for class_name in class_names:
            with self.subTest(class_name=class_name):
                with patch("sys.stdout", new=StringIO()) as output:
                    self.assertFalse(HBNBCommand().onecmd(
                        f"create {class_name}"))
                    test_id = output.getvalue().strip()
                with patch("sys.stdout", new=StringIO()) as output:
                    obj = storage.all()[f"{class_name}.{test_id}"]
                    command = f"show {class_name} {test_id}"
                    self.assertFalse(HBNBCommand().onecmd(command))
                    self.assertEqual(obj.__str__(), output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
