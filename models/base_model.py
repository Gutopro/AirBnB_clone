#!/usr/bin/env python3
"""A base class model for an Airbnb clone.

This class saves the date, id, and time that an instance was created.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class that defines common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """The class constructor.

        Initializes instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the official string representation of the class."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the `updated_at` attribute and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys and values of `__dict__`."""
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = type(self).__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict
