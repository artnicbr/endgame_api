from flask_restful import Resource
from flask import request
from ..Authenticator import Authenticator

class Version(Resource):
    def get(self):
        return {'version': '0.0.1'}