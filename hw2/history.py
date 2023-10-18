"""
displays quotes already stored in the backend to the user
"""


from flask import render_template
from flask.views import MethodView
from data_model import get_model
from lib.quote import Quote


class History(MethodView):
    

    def get(self):
        model = get_model()
        quotes = model.select()
        return render_template('history.html', quotes=quotes)
