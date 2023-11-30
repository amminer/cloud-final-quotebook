"""
currently using https://cloud.google.com/vertex-ai/docs/generative-ai/start/quickstarts/quickstart-text
Remember to set the GOOGLE_APPLICATION_CREDENTIALS env var to the path to the
service account key JSON file... Also ensure that the following have been run? Need to sort this out for deployment...
gcloud auth application-default login
gcloud auth application-default set-quota-project cloud-miner-amminer
"""


import json
import vertexai
from vertexai.language_models import TextGenerationModel


def verify_quote(quote):
    """
    Use google cloud's text analysis API to determine whether a quote is real
    :param quote: Quote object to verify
    :return: json {
      'verifiable': bool, whether there is sufficient information to verify,
      'verified': bool, whether the quote is deemed real
    }
    """
    project_id = 'cloud-miner-amminer'
    temperature = 0.1
    max_output_tokens = 100
    top_p = 0.95  # default
    top_k = 40  # default
    prompt = f'''
    Format your response to this prompt as JSON with keys "verifiable" and "verified",
    and boolean values. The response text will be ingested by code and parsed as JSON,
    so DO NOT format it for human viewing; i.e. the response MUST be valid JSON
    with no other characters. DO NOT surround the JSON with backticks or other formatting.
    Consider the entity "{quote.who}".
    Is sufficient information about this entity present on the internet
    such that a quote claimed to be from them could be verified with reasonable ease and certainty?
    If so, do your best to determine whether this quote of theirs is real:
    "{quote.quote}"
    Be very strict about this, preferring to mark a quote as not verifiable -
    if you don't know whether the source of the quote is well-known,
    assume that they are not.
    '''

    vertexai.init(project=project_id, location='us-west1')
    parameters = {
      'temperature': temperature,
      'max_output_tokens': max_output_tokens,
      'top_p': top_p,
      'top_k': top_k
    }
    model = TextGenerationModel.from_pretrained('text-bison')
    response = model.predict(prompt, **parameters)
    return json.loads(response.text)


if __name__ == '__main__':
  from sys import path
  path.append('/home/meelz/school/cloud-miner-amminer/final/')
  from lib.quote import Quote
  quote = Quote(quote='I am the greatest', who='Muhammad Ali')
  print(f'expecting true, true:\n{verify_quote(quote)}')
  quote = Quote(quote='I am pretty good at boxing, I guess', who='Muhammad Ali')
  print(f'expecting true, false:\n{verify_quote(quote)}')
  # This next test proved really interesting and caused me to rework my prompt
  # and, consequentially, the way that the return value is parsed.
  # When I force the model to strictly return valid JSON (to make my life easy),
  # it would return true, true, even though this quote is obviously not "real".
  # However, when I allow the model to return conversational text followed by valid JSON,
  # it returns false, false, as expected. Very strange and confusing behavior.
  # Notably, ChatGPT from OpenAI does not behave this way,
  # but I have no way to use it programmatically for free, so I have to settle for
  # this Google™️ nonsense.
  quote = Quote(quote='I am goated with the sauce tbh fam', who='yung saucy goat (very famous rapper)')
  print(f'expecting false, false:\n{verify_quote(quote)}')
