"""
displays quotes already stored in the backend to the user
"""


from flask import render_template
from flask.views import MethodView
import urllib

from data_model import get_model
from lib.date_helper import date_to_string


class History(MethodView):
    

    def get(self):
        model = get_model()
        quotes = model.select()
        lnks = ['https://en.wikiquote.org/wiki/' + urllib.parse.quote(quote.who) if quote.verifiable
                else 'https://en.wikiquote.org/wiki/Main_Page'
                for quote in quotes]
        quotes = list(zip(quotes, lnks))
        return render_template('history.html', quotes=quotes, date_to_string=date_to_string)
