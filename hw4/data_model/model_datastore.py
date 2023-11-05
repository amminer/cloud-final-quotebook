"""
In order to use this module, the app must be run in an environment containing a
service account key file. Set the env var GOOGLE_APPLICATION_CREDENTIALS to
the path to the key file. If you're running in a container, you can copy the
file into the container's filesystem per-instance (-v containerpath:localpath
in docker)
"""
from data_model.Model import BaseModel
from lib.quote import Quote
from lib.date_helper import date_to_string
from google.cloud import datastore


PROJECT_NAME = 'cloud-miner-amminer'


def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ quote, who, when, where, how, context ]
    quote, who, where, how, and context: str
    when: datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['quote'], entity['who'], entity['when'], entity['where'],
            entity['how'], entity['context']]


class Model(BaseModel):


    def __init__(self):
        self.client = datastore.Client(PROJECT_NAME)


    def select(self):
        """
        Get all entries from the database
        :return: List of Quote objects populated from the database rows
        """
        query = self.client.query(kind = 'Quote')
        google_response = query.fetch()
        quote_lists = list(map(from_datastore, google_response))
        quotes = [Quote(*quote_list) for quote_list in quote_lists]
        return quotes


    def insert(self, quote: Quote):
        """
        Insert a new entry into the database
        :param quote: Quote object to insert
        :return: None
        """
        key = self.client.key('Quote')
        entity = datastore.Entity(key)
        entity.update( {
            'quote': quote.quote,
            'who': quote.who,
            'when': quote.when,
            'where': quote.where,
            'how': quote.how,
            'context': quote.context
            })
        self.client.put(entity)
        return True
