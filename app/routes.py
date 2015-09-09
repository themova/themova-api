from flask import Blueprint
from flask.ext.restful import Api

from app import resources


bp_api = Blueprint('bp_api', __name__)
api = Api(bp_api, catch_all_404s=True)

api.add_resource(resources.HomeResource, '/')
api.add_resource(resources.TranslationListResource, '/translation/')
api.add_resource(resources.TranslationResource,
                 '/translation/<int:translation_id>')
