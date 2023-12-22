from flask_restful import Resource
from flask import request

class Authenticator(Resource):
    mysql = None

    @classmethod
    def setDatabase(self, param):
        self.mysql = param

    def put(self):
        status = 200
        result = None
        message = None

        try:
            api_user = request.json["user"]
            api_key = request.json["key"]

            cursor = self.mysql.connection.cursor()
            result = cursor.callproc('genApiToken',[api_user, api_key])
        except Exception as ex:
            status = 500
            message = str(ex)

        return {
            "status": status, 
            "result": result, 
            "message": message
        }
    
    def post(self):
        status = 200
        result = None
        message = None

        try:
            api_token = request.headers.get("token")

            cursor = self.mysql.connection.cursor()
            result = cursor.callproc('checkApiToken',[api_token])
        except Exception as ex:
            status = 500
            message = str(ex)

        return {
            "status": status, 
            "result": result, 
            "message": message
        }