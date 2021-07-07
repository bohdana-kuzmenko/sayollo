from http import HTTPStatus

from flask import Response, make_response


def make_custom_response(fn):
    def wrapped(self, *args, **kwargs):
        try:
            response = fn(self, *args, **kwargs)
        except Exception as e:
            response = make_response(
                getattr(e, 'message', repr(e)),
                HTTPStatus.INTERNAL_SERVER_ERROR)
        else:
            if not isinstance(response, Response):
                response = make_response(response, HTTPStatus.OK)
        finally:
            return response

    return wrapped
