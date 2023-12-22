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

            sql = '''SELECT genApiToken(%s, %s)'''
            cursor = self.mysql.connection.cursor()
            cursor.execute(sql,[api_user, api_key])
            result = cursor.fetchone()[0]

        except Exception as ex:
            status = 500
            message = str(ex)

        r = {
            "result": result, 
            "message": message
        }

        return r, status
    
    def post(self):
        status = 200
        result = None
        message = None

        try:
            api_token = request.headers.get("token")

            sql = '''SELECT checkApiToken(%s) as CK'''
            cursor = self.mysql.connection.cursor()
            cursor.execute(sql, (api_token,))
            result = True if cursor.fetchone()[0] == 1 else False

        except Exception as ex:
            status = 500
            message = str(ex)

        r = {
            "result": result, 
            "message": message
        }

        return r, status