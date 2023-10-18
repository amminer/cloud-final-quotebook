"""
TODO docs
"""

from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from data_model import get_model
from lib.quote import Quote


class Contribute(MethodView):
    def get(self):
        return render_template('contribute.html')
    
    def post(self):
        model = get_model()
        quote = Quote(
            quote=request.form['quote'],
            who=request.form['who'],
            when=request.form['when'],
            where=request.form['where'],
            how=request.form['how'],
            context=request.form['context']
        )
        model.insert(quote)
        return redirect(url_for('history'))
