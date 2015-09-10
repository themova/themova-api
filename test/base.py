from flask import Flask
from flask.ext.testing import TestCase
from app.routes import bp_api


class BaseThemovaTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(bp_api)
        return app
