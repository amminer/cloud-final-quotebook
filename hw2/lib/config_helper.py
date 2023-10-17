"""
TODO docs
"""


import json


class ConfigParser():
    

    def __init__(self, config_file_path='config.json'):
        self.read_in_from_file(config_file_path)


    def read_in_from_file(self, file_path):
        with open(file_path, 'r') as raw_file:
            self.raw_content = ''.join(raw_file.readlines())
        self.json = json.loads(self.raw_content)

        self.model = self.json['model']


config = ConfigParser()
