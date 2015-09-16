from flask import jsonify
from flask.ext.restful import Resource
from marshmallow import fields, Schema, ValidationError

from app import app
from app.models.translation import Translation
from app.utils import dump_with, load_with


def not_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class TranslationSchema(Schema):
    title = fields.String(required=True, validate=not_blank)
    text = fields.Email(required=True, validate=not_blank, load_only=True)


@app.errorhandler(ValidationError)
def validation_handler(error):
    response = jsonify({'errors': error.messages})
    response.status_code = 400
    return response


class HomeResource(Resource):
    def get(self):
        return {'message': 'TheMova API'}


class TranslationListResource(Resource):

    @dump_with(TranslationSchema)
    def get(self):
        return Translation.get_all()

    @dump_with(TranslationSchema)
    @load_with(TranslationSchema)
    def post(self, params):
        return Translation.create(params['title'], params['text']), 201


class TranslationResource(Resource):

    @dump_with(TranslationSchema)
    def get(self, translation_id):
        return Translation.query.get_or_404(translation_id)

    def put(self, translation_id, title):
        pass

    def delete(self, translation_id):
        pass
