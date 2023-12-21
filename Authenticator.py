from flask_restful import Resource
from flask import request

class Authenticator(Resource):
    mysql = None

    @classmethod
    def setDatabase(self, param):
        self.mysql = param

    def put(self):
        api_user = request.json["user"]
        api_key = request.json["key"]

        cursor = self.mysql.connection.cursor()
        result = cursor.callproc('genApiToken',[api_user, api_key])

        return {"status": 200, "result": result}