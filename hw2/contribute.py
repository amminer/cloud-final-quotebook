"""
form for contributing a quote to the backend
"""


from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from datetime import datetime
from data_model import get_model
from lib.quote import Quote
from lib.date_helper import string_to_date


class Contribute(MethodView):


    def get(self):
        return render_template('contribute.html')
    

    def post(self):
        quote = request.form['quote']
        who = request.form['who']
        if not quote or not who:
            return render_template('contribute.html', error='Please fill out all required fields')
        when = request.form['when']
        where = request.form['where']
        when = string_to_date(request.form['when'])
        quote = Quote(
            quote=request.form['quote'],
            who=request.form['who'],
            when=when,
            where=request.form['where'],
            how=request.form['how'],
            context=request.form['context']
        )
        model = get_model()
        print(f'INFO: inserting {quote}', flush=True) # TODO logging?
        model.insert(quote)
        return redirect(url_for('history'))
