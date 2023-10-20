"""
implements the Model interface for sqlite3
"""


import sqlite3
from data_model.Model import BaseModel
from lib.quote import Quote
from lib.date_helper import date_to_string


class Model(BaseModel):


    def __init__(self):
        """
        create the sqlite database file or open the existing file,
        create the quotes table if it does not exist
        """
        self.connection = sqlite3.connect('quotes.db') # will create if not exists
        cur = self.connection.cursor()
        try:
            cur.execute("select count(rowid) from quotes")
        except sqlite3.OperationalError:
            cur.execute(
                '''
                create table quotes (
                quote text,
                who text,
                _when date,
                _where text,
                how text,
                context text
                );
                '''
            )
        cur.close()


    def select(self):
        """
        Get all entries from the database
        :return: List of Quote objects populated from the database rows
        """
        cur = self.connection.cursor()
        raw_quotes = cur.execute('SELECT * FROM quotes').fetchall()
        quotes = [Quote(*raw_quote) for raw_quote in raw_quotes]
        cur.close()
        return quotes


    def insert(self, quote: Quote):
        """
        Insert a new entry into the database
        :param quote: Quote object to insert
        :return: None
        """
        cur = self.connection.cursor()
        insert_query = f'''
            insert into quotes (quote, who, _when, _where, how, context)
            values ("{quote.quote}", "{quote.who}", date("{date_to_string(quote.when)}"), "{quote.where}",
                    "{quote.how}", "{quote.context}")
            '''
        cur.execute(insert_query)
        self.connection.commit()
        cur.close()
        return None
