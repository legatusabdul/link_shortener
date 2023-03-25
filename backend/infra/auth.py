from functools import wraps
from itsdangerous import BadSignature
from http import HTTPStatus

from flask import request, jsonify, make_response


def requires_auth(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return make_response(jsonify("Missing auth token!"), HTTPStatus.UNAUTHORIZED)
        
        try:
            if not token == "sUpeRSecr3t!Str1ng":  # Must be encryption/decryption mechanism in the product version
                raise BadSignature("Bad auth token!")
        except BadSignature as e:
            return make_response(jsonify(e.message), HTTPStatus.UNAUTHORIZED)
        
        return func(*args, **kwargs)
    return wrapper
