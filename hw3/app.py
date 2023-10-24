"""
CS530 F23 - amminer - HW2
A simple web application for famous quotes
REQUIREMENTS:
 * Follows an MVP pattern and supports the following routes/views:
  - Route that implements the default landing page with links to other routes
  - Route that allows one to view all entries previously submitted
  - Route for creating/inserting new entries via an HTML form

 * Have a backend implementation that has:
  - An abstract model class (e.g. Model.py) that supports
   + individual fields with varying data types to support the application and
   + that is documented via Docstrings including parameters and return values with their types
  - A derived data model class (e.g. model_sqlite3.py) that supports
   + creation and reading of entries via a sqlite3 database
"""


import flask
from index import Index
from history import History
from contribute import Contribute


APP = flask.Flask(__name__)


"""
landing page with links to other routes; linked to by header at top of layout
"""
APP.add_url_rule(
    rule='/',
    view_func=Index.as_view('index'),
    methods=['GET']
)


"""
allows users to submit new quotes
"""
APP.add_url_rule(
    rule='/contribute',
    view_func=Contribute.as_view('contribute'),
    methods=['GET','POST']
)


"""
allows users to view all existing quotes
"""
APP.add_url_rule(
    rule='/history',
    view_func=History.as_view('history'),
    methods=['GET']
)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000, debug=True)
