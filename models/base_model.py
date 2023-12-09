#!/usr/bin/python3
"""base model module"""
import uuid
from datetime import datetime


class BaseModel:
    """ca base class"""
    def __init__(self):
        """initiates the class"""

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
