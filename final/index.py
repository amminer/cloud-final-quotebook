"""
landing page with links to other routes
"""


from flask import render_template
from flask.views import MethodView
from lib.quote import Quote
#from app import ROUTES # TODO work around circular import
# for now do it manually


class Index(MethodView):


    def get(self):
        routes = {
            'history': '/history',
            'contribute': '/contribute'
        }
        return render_template('index.html', other_routes=routes)
