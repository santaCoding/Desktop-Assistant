import json
import os

class DB(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def getDB(self):
        return self.db

    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"), indent=4)
            return True
        except:
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
        except Exception as e:
            return False

    def setValue(self, nickname, value, operator):
        temp_dict = self.db[nickname]
        temp_dict[operator] = value
        self.db[nickname] = temp_dict
        self.dumpdb()
        return True

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
    
    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True
