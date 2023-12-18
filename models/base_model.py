#!/usr/bin/python3
"""base model module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for AirBnB clone"""
    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    try:
                        value = datetime.fromisoformat(value)
                    except ValueError:
                        raise ValueError(f"Invalid datetime format for {key}")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the time of any incoming update"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Prints the class name and id"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Returns a dictionary containing all the class attributes"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
