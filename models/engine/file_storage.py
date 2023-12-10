#!/usr/bin/python3
""" file storage class definition """
from models.base_model import BaseModel
import json


class FileStorage:
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized, file)

    def saves(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def my_save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            # Deserializes the JSON file to __objects
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    # Create an instance from the dictionary
                    # representation and add to __objects
                    # Explicitly import the class based on its name
                    class_module = globals().get(class_name)
                    if class_module:
                        self.__objects[key] = class_module(**value)
                    # self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass  # If the file doesn't exist, do nothing
