#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        if cls is not None:
            filterjs = {}
            for key, value in self.__objects.items():
                # find the name of the class
                if value.__class__.name__ == cls.__name__:
                    # add to the filtered dictionary
                    filterjs[key] = value
            return filterjs
        else:
            return FileStorage.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
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
        '''
        delete obj from __objects
        '''
        if obj is not None:
            # pull obj key and define it in variable
            key = obj.__class__.__name__ + "." + obj.id
            # If key is found in the dictionar, use key to delete object.
            if key in self.__objects:
                self.__objects.pop(key)
        else:
            return

    def close(self):
        '''
        deserialize JSON file to object
        '''
        self.reload()
