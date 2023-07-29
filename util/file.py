import json

class File:
    
    def __init__(self, name):
        self.name = name
        
    def get_property(self, prop):
        with open(self.name) as file:
            file = json.load(file)
            
        return file[prop]