"""
TODO docs
"""

from flask import render_template
from flask.views import MethodView
from data_model import get_model
from lib.quote import Quote


class Index(MethodView):
    def get(self):
        model = get_model()
        quotes = [Quote(quote   =   row[0],
                        who     =   row[1],
                        when    =   row[2],
                        where   =   row[3],
                        how     =   row[4],
                        context =   row[5])
            for row in model.select()]
        return render_template('index.html', quotes=quotes)
