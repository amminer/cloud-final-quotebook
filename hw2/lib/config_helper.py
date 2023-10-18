"""
reads in the configuration information for the app,
which is stored in a JSON file, /config.json by default

client code should import the config object from this module
and read its properties to determine the configuration of the app
"""


import json


class _ConfigParser():
    

    def __init__(self, config_file_path='config.json'):
        self.read_in_from_file(config_file_path)


    def read_in_from_file(self, file_path):
        with open(file_path, 'r') as raw_file:
            self.raw_content = ''.join(raw_file.readlines())
        self.json_dict = json.loads(self.raw_content)

        for key, val in self.json_dict.items():
            self.__dict__[key] = val
        #self.model = self.json['model']


config = _ConfigParser()
