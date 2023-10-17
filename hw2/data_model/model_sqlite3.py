"""
TODO docs
"""


import sqlite3
from data_model.Model import BaseModel
from lib.quote import Quote


class Model(BaseModel):
    pass # TODO


    def select(self):
        return [
            Quote('It is Wednesday my dudes', 'Jimmy Here'),
            Quote('Our scientific power has outrun our spiritual power. '
                  + 'We have guided missiles and misguided men.',
                  'Martin Luther King, Jr.', when='1963')
        ] # TODO


    def insert(self):
        return None # TODO
