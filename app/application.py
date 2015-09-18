import os

from flask import Flask

from app import models  # noqa
from app.errors import add_error_handlers
from app.routes import bp_api
from app.extensions import db, migrate


def create_app(config=None):
    app = Flask(__name__)
    config_file = os.environ.get('CONFIG_FILE_PATH', 'config')
    app.config.from_object(config_file)
    if config:
        app.config.from_pyfile(config)

    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    app.register_blueprint(bp_api)
    extensions_fabrics(app)
    add_error_handlers(app)
    return app


def extensions_fabrics(app):
    db.init_app(app)
    migrate.init_app(app, db)
