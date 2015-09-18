import os

import flask
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
config_file = os.environ.get('CONFIG_FILE_PATH', 'config')
app.config.from_object(config_file)
database_url = os.environ.get('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import bp_api
app.register_blueprint(bp_api)
from app import models  # noqa
