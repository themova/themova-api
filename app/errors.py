from flask import jsonify
from marshmallow import ValidationError


def add_error_handlers(app):
    @app.errorhandler(ValidationError)
    def validation_handler(error):
        response = jsonify({'errors': error.messages})
        response.status_code = 422
        return response
