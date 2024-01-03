#!/usr/bin/python3
"""
 model FileStorage
"""
import json
import models


class FileStorage:
    """
       class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return dictionary
        """
        if cls:
            my_dict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls:
                    my_dict[key] = value
            return my_dict
        return self.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serialize __objects attribute to JSON file.
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
            Deserialize the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
       method to delete obj from __objects
        """
        copy = dict(FileStorage.__objects)
        for key, value in copy.items():
            if value == obj:
                del FileStorage.__objects[key]
            self.save()

    def close(self):
        """
        Closing the Engine after Deserializing JSON File to __objects
        """
        self.reload()
