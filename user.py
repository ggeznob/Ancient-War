import jsonpickle

from path import *
from setting import *


def save(data, path = level_data_path):
    data = jsonpickle.encode(data)
    with open(path, "w") as file:
        file.write(data)


def load(path = level_data_path):
    with open(path, "r") as file:
        data = file.read()
    data = jsonpickle.decode(data)
    return data


class LevelData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LevelData, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        try:
            self.data = load(level_data_path)
        except FileNotFoundError:
            self.data = {'level_access': [False] * 8, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
            self.data['level_access'][0] = True
            save(self.data, level_data_path)

    def get_level(self, levelnum):
        self.data['level_access'][levelnum - 1] = True
        save(self.data, level_data_path)
        self.data = load(level_data_path)

    def save_score(self, levelnum, score):
        self.data[levelnum] = score
        save(self.data, level_data_path)
        self.data = load(level_data_path)
