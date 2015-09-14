from functools import wraps

from flask_restful.utils import unpack


def marshal(data, schema, envelope=None):
    """Takes raw data (in the form of a dict, list, object) and a dict of
    fields to output and filters the data based on those fields.

    :param data: the actual object(s) from which the fields are taken from
    :param fields: a dict of whose keys will make up the final serialized
                   response output
    :param envelope: optional key that will be used to envelop the serialized
                     response


    >>> from flask_restful import fields, marshal
    >>> data = { 'a': 100, 'b': 'foo' }
    >>> mfields = { 'a': fields.Raw }

    >>> marshal(data, mfields)
    OrderedDict([('a', 100)])

    >>> marshal(data, mfields, envelope='data')
    OrderedDict([('data', OrderedDict([('a', 100)]))])

    """

    many = False

    if isinstance(data, (list, tuple)):
        many = True

    if isinstance(schema, type):
        schema = schema(many=many)

    result = schema.dump(data).data
    return ({'envelope': result} if envelope else result)


def marshal_with(schema, envelope=None):
    """A decorator that apply marshalling to the return values of your methods.

    >>> from flask_restful import fields, marshal_with
    >>> mfields = { 'a': fields.Raw }
    >>> @marshal_with(mfields)
    ... def get():
    ...     return { 'a': 100, 'b': 'foo' }
    ...
    ...
    >>> get()
    OrderedDict([('a', 100)])

    >>> @marshal_with(mfields, envelope='data')
    ... def get():
    ...     return { 'a': 100, 'b': 'foo' }
    ...
    ...
    >>> get()
    OrderedDict([('data', OrderedDict([('a', 100)]))])

    """
    """
    :param fields: a dict of whose keys will make up the final
                    serialized response output
    :param envelope: optional key that will be used to envelop the serialized
                        response
    """
    def wrapper(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                if not data.get('error'):
                    data = marshal(data, schema, envelope)
                return data, code, headers
            else:
                return marshal(resp, schema, envelope)
        return func_wrapper

    return wrapper
