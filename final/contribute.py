"""
form for contributing a quote to the backend
"""


from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from datetime import datetime
from data_model import get_model
from lib.quote import Quote
from lib.date_helper import string_to_date
from lib.random_quotes_helper import get_random_quote, CATEGORIES


class Contribute(MethodView):


    def get(self):
        return render_template('contribute.html', categories=CATEGORIES)
    

    def post(self):
        if 'lazy' in request.form.keys():
            category = request.form['category']
            quote = get_random_quote(category if category != 'random' else None)
        else:
            quote_text = request.form['quote']
            who = request.form['who']
            if not quote_text or not who:
                return render_template('contribute.html',
                    error='Please fill out all required fields')
            where = request.form['where']
            when = string_to_date(request.form['when'])
            how = request.form['how']
            context = request.form['context']
            quote = Quote(
                quote=quote_text,
                who=who,
                when=when,
                where=where,
                how=how,
                context=context
            )
        model = get_model()
        print(f'INFO: inserting {quote}', flush=True) # TODO logging?
        model.insert(quote)
        return redirect(url_for('history'))
