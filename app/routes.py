from flask import Blueprint
from flask.ext.restful import Api

from app import resources


bp_api = Blueprint('bp_api', __name__)
api = Api(bp_api)

api.add_resource(resources.HomeResource, '/')
