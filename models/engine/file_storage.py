#!/usr/bin/python3
"""file storage module"""
from models.base_model import BaseModel
import json
import os


class FileStorage():
    """file storage class that serializes
    instances to json file and deserializes
    json files to instances"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dict objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """saves a new object"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes to json file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {key:value.to_dict() for key, value in FileStorage.__objects.items()}, f)
            
    def reload(self):
        """deserializes json file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for value in objs.values():
                    clas = value["__class__"]
                    self.new(eval(clas)(**value))
        except Exception:
            pass