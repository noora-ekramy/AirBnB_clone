#!/usr/bin/python3
"""base model module"""
import uuid
from datetime import datetime


class BaseModel:
    """ca base class"""
    def __init__(self, *args, **kwargs):
        """initiates the class"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """update the time of any incoming update"""
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the name and id"""
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """return a dictionary containing all the base class attributes"""
        new_dic = self.__dict__.copy()
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        new_dic["__class__"] = self.__class__.__name__
        return new_dic
