from functools import wraps

from flask import request
from flask_restful.utils import unpack


def marshal(data, schema, envelope=None):
    """Takes raw data (in the form of a dict, list, object) and a schema for
    marshaling and filters the data based on this schema.

    :param data: the actual object(s) from which the fields are taken from
    :param schema: a type or instance of Schema class with fields definition
    :param envelope: optional key that will be used to envelop the serialized
                     response
    """
    many = isinstance(data, (list, tuple))

    result = schema.dump(data, many=many).data
    return ({'envelope': result} if envelope else result)


def dump_with(schema, envelope=None):
    """A decorator that apply marshalling to the return values of your methods.

    :param schema: a type or instance of Schema class with fields definition
    :param envelope: optional key that will be used to envelop the serialized
                     response
    """
    if isinstance(schema, type):
        schema = schema()

    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                data = marshal(data, schema, envelope)
                return data, code, headers
            else:
                return marshal(resp, schema, envelope)
        return func_wrapper

    return wrapper


def load_with(schema):
    """A decorator that apply marshalling to the return values of your methods.

    :param schema: a type or instance of Schema class with fields definition
    """

    if isinstance(schema, type):
        schema = schema(strict=True)

    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            json_data = request.get_json()
            many = isinstance(json_data, list)

            params = schema.load(json_data, many=many).data
            return f(params=params, *args, **kwargs)
        return func_wrapper

    return wrapper
