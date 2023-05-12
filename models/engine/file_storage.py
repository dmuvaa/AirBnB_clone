#usr/bin/python3

"""creates aclass."""

import json
import os


class FileStorage:
    """class that that serializes instances to a JSON file."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """."""
        return self.__objects

    def new(self, obj):
        """function method that sets objects with key."""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """func method to serialize object to JSON file path."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() /
                for k, v in self.__objects.items()}, f)

    def reload(self):
        """func method to deserialize JSON file."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for k, v in objs.items():
                self.__objects[k] = BaseModel(**v)
