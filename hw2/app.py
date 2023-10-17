"""
CS530 F23 - amminer - HW2
A simple web application for famous quotes
REQUIREMENTS:
 * Follows an MVP pattern and supports the following routes/views:
  - Route that implements the default landing page with links to other routes
  - Route that allows one to view all entries previously submitted
  - Route for creating/inserting a new entries via an HTML form

 * Have a backend implementation that has:
  - An abstract model class (e.g. Model.py) that supports
   + individual fields with varying data types to support the application and
   + that is documented via Docstrings including parameters and return values with their types
  - A derived data model class (e.g. model_sqlite3.py) that supports
   + creation and reading of entries via a sqlite3 database
"""

import flask
from flask.views import MethodView
from index import Index
#from contribute import Contribute # TODO

app = flask.Flask(__name__)

app.add_url_rule(
    rule='/',
    view_func=Index.as_view('index'),
    methods=['GET']
)

#app.add_url_rule( # TODO
    #endpoint='/contribute',
    #view_func=Contribute.as_view('contribute'),
    #methods=['GET','POST']
#)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
