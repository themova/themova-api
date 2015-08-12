import flask
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

app = flask.Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import bp_api
app.register_blueprint(bp_api)
from app import models
