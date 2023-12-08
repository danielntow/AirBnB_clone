#!/usr/bin/python3
""" a module that defines the base model ls"""
import uuid
from datetime import datetime
# from models import storage
import models


class BaseModel:
    """BaseModel class that defines common -
       attributes/methods for other classes

    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance with unique id and timestamps."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())  # Assign unique ID if not provided
            # Record creation time if not provided
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                # Record last update time if not provided
                self.updated_at = datetime.now()

        else:
            # If kwargs is empty,create new inst w/ unique id and current date
            self.id = str(uuid.uuid4())  # Assign unique ID
            self.created_at = datetime.now()  # Record creation time
            self.updated_at = datetime.now()  # Record last update time
            # Add the new instance to the storage
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        # Call save method of models.storage
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Contains keys/values of instance attributes,
                  including class name, creation,
                  and update timestamps in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__  # Add class name
        # Convert to ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        # Convert to ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
