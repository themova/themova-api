import flask
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

app = flask.Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app.resources import HomeResource

api.add_resource(HomeResource, '/')
