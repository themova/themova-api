from flask import request
from flask.ext.restful import Resource

from marshmallow import fields, Schema, ValidationError

from app.models.translation import Translation
from app.utils import marshal_with


def not_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class TranslationSchema(Schema):
    title = fields.Str(required=True, validate=not_blank)
    text = fields.Str(required=True, validate=not_blank)


class HomeResource(Resource):
    def get(self):
        return {'message': 'TheMova API'}


class TranslationListResource(Resource):

    @marshal_with(TranslationSchema)
    def get(self):
        return Translation.get_all()

    @marshal_with(TranslationSchema)
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'error': 'No input data provided.'}, 400
        translation_schema = TranslationSchema()
        data, errors = translation_schema.load(json_data)
        if errors:
            return {'error': errors}, 422

        translation = Translation.create(data['title'], data['text'])
        return translation, 201


class TranslationResource(Resource):

    @marshal_with(TranslationSchema)
    def get(self, translation_id):
        return Translation.query.get_or_404(translation_id)

    def put(self, translation_id, title):
        pass

    def delete(self, translation_id):
        pass
