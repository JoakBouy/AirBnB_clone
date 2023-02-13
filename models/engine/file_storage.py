import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise, do nothing)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
