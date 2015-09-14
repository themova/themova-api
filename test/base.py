import json

from flask import Flask
from flask.ext.testing import TestCase
from flask.testing import FlaskClient

from app.routes import bp_api


class JsonFlaskClient(FlaskClient):

    def post(self, *args, **kw):
        """ POST method will be used mostly for json data"""
        if 'data' in kw:
            try:
                kw['data'] = json.dumps(kw['data'])
            except TypeError:
                pass
        if not kw.get('content_type'):
            kw['content_type'] = 'application/json'
        return super(JsonFlaskClient, self).post(*args, **kw)

    def put(self, *args, **kw):
        """PUT method will be used mostly for json data"""
        if 'data' in kw:
            try:
                kw['data'] = json.dumps(kw['data'])
            except TypeError:
                pass
        if not kw.get('content_type'):
            kw['content_type'] = 'application/json'
        return super(JsonFlaskClient, self).put(*args, **kw)


class BaseThemovaTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        app.test_client_class = JsonFlaskClient
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.sqlite'
        app.register_blueprint(bp_api)
        return app
