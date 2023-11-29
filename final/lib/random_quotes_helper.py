"""
Remember to set the API_NINJA_KEY env var if running locally
currently using https://api-ninjas.com/api/quotes
"""


import requests
from os import environ

from .quote import Quote
from .exceptions import APIError


CATEGORIES = [
  'age',
  'alone',
  'amazing',
  'anger',
  'architecture',
  'art',
  'attitude',
  'beauty',
  'best',
  'birthday',
  'business',
  'car',
  'change',
  'communications',
  'computers',
  'cool',
  'courage',
  'dad',
  'dating',
  'death',
  'design',
  'dreams',
  'education',
  'environmental',
  'equality',
  'experience',
  'failure',
  'faith',
  'family',
  'famous',
  'fear',
  'fitness',
  'food',
  'forgiveness',
  'freedom',
  'friendship',
  'funny',
  'future',
  'god',
  'good',
  'government',
  'graduation',
  'great',
  'happiness',
  'health',
  'history',
  'home',
  'hope',
  'humor',
  'imagination',
  'inspirational',
  'intelligence',
  'jealousy',
  'knowledge',
  'leadership',
  'learning',
  'legal',
  'life',
  'love',
  'marriage',
  'medical',
  'men',
  'mom',
  'money',
  'morning',
  'movies',
  'success']


def get_random_quote(category=None):
    """
    Get a random quote from the API
    :param category: str, the category of the quote, optional
    :return: Quote object populated from the API response
    May throw ValueError on bad category or APIError on return code != 200
    """
    if category is not None and category not in CATEGORIES:
        raise ValueError('Invalid category')

    url = 'https://api.api-ninjas.com/v1/quotes'
    url += '?category=' + category if category is not None else ''
    key = environ.get('API_NINJA_KEY')
    headers = {'X-Api-Key': key}

    response = requests.request('GET', url, headers=headers)

    if response.status_code == 200:
        response_content = response.json()[0]
        return Quote(
            quote=response_content['quote'],
            who=response_content['author']
        )
    else:
        raise APIError('Random quotes API', response.status_code)
