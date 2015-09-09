from flask import request
from flask.ext.restful import Resource

from marshmallow import fields, Schema, ValidationError

from app.models.translation import Translation


def not_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class TranslationSchema(Schema):
    title = fields.Str(required=True, validate=not_blank)
    text = fields.Str(required=True, validate=not_blank)


translation_schema = TranslationSchema()
translations_schema = TranslationSchema(many=True)


class HomeResource(Resource):
    def get(self):
        return {'message': 'TheMova API'}


class TranslationListResource(Resource):

    def get(self):
        translations = Translation.get_all()
        result = translations_schema.dump(translations)
        return {'response': result.data}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'error': 'No input data provided.'}, 400
        data, errors = translation_schema.load(json_data)
        if errors:
            return {'error': errors}, 422

        translation = Translation.create(data['title'],
                                         data['text'])
        result = translation_schema.dump(translation)
        return {'message': 'Created new translation.',
                'response': result.data}


class TranslationResource(Resource):

    def get(self, translation_id):
        translation = Translation.query.get_or_404(translation_id)
        result = translation_schema.dump(translation)
        return {'response': result.data}

    def put(self, translation_id, title):
        pass

    def delete(self, translation_id):
        pass
