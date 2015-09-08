from flask import request
from flask.ext.restful import Resource

from marshmallow import fields, Schema, ValidationError
from werkzeug.exceptions import NotFound

from app.models.translation import Translation


def not_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

class TranslationSchema(Schema):
     title = fields.Str(required=True, validate=not_blank)
     text = fields.Str(required=True, validate=not_blank)


translationschema = TranslationSchema()
translationsschema = TranslationSchema(many=True)


class HomeResource(Resource):
    def get(self):
        return {'message': 'TheMova API'}


class TranslationListResource(Resource):

    def get(self):
        translations = Translation.get_all()
        result = translationsschema.dump(translations)
        return {'response': result.data}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'error': 'No input data provided.'}, 400
        data, errors = translationschema.load(json_data)
        if errors:
            return {'error': errors}, 422

        translation = Translation.create(data['title'],
                                         data['text'])
        result = translationschema.dump(translation)
        return {'message': 'Created new translation.',
                'response': result.data}


class TranslationResource(Resource):

    def get(self, translation_id):
        translation = Translation.get(translation_id)
        if translation:
            result = translationschema.dump(translation)
            return {'response': result.data}
        raise NotFound

    def put(self, translation_id, title):
        pass

    def delete(self, translation_id):
        pass
