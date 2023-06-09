#!/usr/bin/python3

""" This module holds the code for a filestorage class """
import os
import json
import sys
import datetime as dt
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This isclass serializes instance to a JSON file and vice versa """

    __file_path = "./file.json"
    __objects = {}

    def destroy_objects(self, obj_id):
        """ update __objects by deleting obj"""
        del FileStorage.__objects[obj_id]

    def update_objects(self, obj_id, key, value):
        """ update __objects by adding or updating key"""
        obj = FileStorage.__objects[obj_id]
        found = 0
        ob = obj.__dict__
        newtime = dt.datetime.now()
        for k, v in ob.items():
            if k == key:
                if type(v) == str:
                    valueN = str(value)
                if type(v) == int:
                    valueN = int(value)
                if type(v) == float:
                    valueN = float(value)
                found = 1
                break
        if found == 0:
            valueN = value
        setattr(obj, key, valueN)
        setattr(obj, 'updated_at', newtime)
        FileStorage.__objects[obj_id] = obj

    def all(self):
        """ This method returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ This method writees to the __object dict
        Args:
            obj: list of objects
        """

        if obj is not None:
            try:
                key = type(obj).__name__ + '.' + obj.id
                FileStorage.__objects[key] = obj
            except Exception as e:
                print(e)

    def save(self):
        """ This method serializes __objects to __file_path """

        with open(FileStorage.__file_path, 'w') as file:
            if FileStorage.__objects is None:
                file.write("[]")
            else:
                ins = {}
                all_objs = self.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    my_model_json = {"__class__": type(obj).__name__}
                    for key, value in obj.__dict__.items():
                        if isinstance(value, dt.datetime):
                            my_model_json[key] = value.isoformat()
                        else:
                            my_model_json[key] = value
                    ins[obj_id] = my_model_json
                file.write(json.dumps(ins, default=str))

    def reload(self):
        """ This method deserializes a JSON obeject to class object """

        class_list = ["User", "State", "City", "Amenity", "Place",
                      "Review", "BaseModel"]

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                listDict = json.load(file)
                obj = {}
                for di in listDict:
                    obj[di] = listDict[di]
                if obj is not None:
                    for k in obj.keys():
                        ob = obj[k]
                        ob_class = ob['__class__']
                        key = ob['__class__'] + '.' + ob['id']
                        if ob_class in class_list:
                            FileStorage.__objects[key] = eval(ob_class)(**ob)
