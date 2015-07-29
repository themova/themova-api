from flask.ext.restful import Resource


class HomeResource(Resource):
    def get(self):
        return {'message': 'TheMova API'}
