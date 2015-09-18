import json
import os

from flask.ext.testing import TestCase
from flask.testing import FlaskClient

from app.application import create_app
from app.extensions import db


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
        """ PUT method will be used mostly for json data"""
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
        config_file = os.environ.get('TEST_CONFIG_FILE_PATH',
                                     '../test/config_test.py')
        app = create_app(config_file)
        test_database_url = os.environ.get('TEST_DATABASE_URL')
        if test_database_url:
            app.config['SQLALCHEMY_DATABASE_URI'] = test_database_url
        app.test_client_class = JsonFlaskClient
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
