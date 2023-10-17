"""
TODO docs
"""


from abc import ABC, abstractclassmethod as ACM
from lib.quote import Quote


class BaseModel(ABC):

    @ACM
    def select(self) -> list[Quote]:
        """
        Get all entries from the database
        :return: List of Quote objects populated from the database rows
        """
        pass

    @ACM
    def insert(self, quote: Quote) -> None:
        """
        Insert a new entry into the database
        :param quote: Quote object to insert
        :return: None
        """
        pass
