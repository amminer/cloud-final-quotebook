"""
https://www.mediawiki.org/wiki/API:Search
"""

import json
import requests
import urllib

#from sys import path  # local debug
#path.append('/home/meelz/school/cloud-miner-amminer/final/')  # local debug
#from lib.quote import Quote  # local debug
from lib.exceptions import APIError


def get_json_from_wq_api(url):
  result = requests.get(url)
  if result.status_code != 200:
    raise APIError('Wikiquote API', result.status_code)
  raw_response = result.content.decode('utf-8')
  return json.loads(raw_response)


def quote_source_is_verifiable_wq(who):
  """
  Use wikiquote's API to determine whether we can check against a quote against
  its source's known quotes.
  Note that there are libraries that provide a higher-level interface for this;
  In python 3.8 or greater, pip install wikiquote and examine the source code.
  :param who: str, source to check for
  :return bool: whether source has a page on wq
  """
  url = 'http://en.wikiquote.org/w/api.php' \
      + '?format=json&action=query&list=search&srlimit=500&srsearch='
  url += urllib.parse.quote(who)
  response_json = get_json_from_wq_api(url)
  results = [entry['title'] for entry in response_json['query']['search']]  # this line is ripped straight from the library code, but it's the only way to parse this JSON...

  # the library does not have the following capability; I may contribute to it at some point
  original_url = url
  while 'continue' in response_json.keys():
    url = original_url + f'&sroffset={response_json["continue"]["sroffset"]}' \
      + f'&continue={response_json["continue"]["continue"]}'
    response_json = get_json_from_wq_api(url)
    results += [entry['title'] for entry in response_json['query']['search']]

  # The API searches titles as well as article content
  return who in results  # So we have to make sure the hit was for a title


def quote_is_legitimate_wq(quote_text, who):
  # TODO try this one from Henry Ford:
  # to do for the world more than the world does for you--that is Success
  # this is an excerpt from a full entry on wq...
  return False  # TODO


#if __name__ == '__main__':  # local debug
  #quote = Quote(quote='I am the greatest', who='Muhammad Ali')  # local debug
  #verify_quote_with_wq(quote)  # local debug
