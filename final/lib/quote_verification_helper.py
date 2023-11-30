import json
import requests
import urllib
from wikiquote.utils import extract_quotes_li
from wikiquote.langs.en import HEADINGS, WORD_BLOCKLIST
import lxml.html

from sys import path  # local debug
path.append('/home/meelz/school/cloud-miner-amminer/final/')  # local debug
from lib.quote import Quote  # local debug
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
  https://www.mediawiki.org/wiki/API:Search
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
  # TODO check for disambiguation page?


def quote_is_legitimate_wq(quote_text, who):
  """
  Should only be called when a quote's source is verifiable as determined
  by quote_source_is_verifiable_wq.
  Lots of room for improvement here, could use string similarity, etc?
  :param quote_text: str, quote to check
  :param who: str, source of quote
  :return bool: whether quote is present on source's wq page
  """
  import wikiquote
  w = wikiquote.quotes('bacon')  # step into this call to see how complicated this can get
  url = 'http://en.wikiquote.org/w/api.php' \
      + '?format=json&action=parse&prop=text|categories&disableeditsection&page='
  url += urllib.parse.quote(who)
  response_json = get_json_from_wq_api(url)
  if 'error' in response_json.keys():  # page probably doesn't exist (shouldn't ever see this in normal operation)
    raise APIError(f'Wikiquote API: {response_json["error"]["info"]}', -1)
  page_body = response_json['parse']['text']['*']
  response_elements = lxml.html.fromstring(page_body)
  # Hopefully this still counts as API integration - see above for why I'm not rolling my own quote parser for now
  parsed_quotes = extract_quotes_li(response_elements, float('inf'), HEADINGS, WORD_BLOCKLIST)
  return any([quote_text in quote for quote in parsed_quotes])


if __name__ == '__main__':  # local debug
  # Unfortunately this is not foolproof... quotes about topics get fact checked as true
  quote = Quote(quote='One bacon does not compare to another.', who='Bacon')  # local debug
  print(quote_source_is_verifiable_wq(quote.who))  # local debug
  print(quote_is_legitimate_wq(quote.quote, quote.who))  # local debug
