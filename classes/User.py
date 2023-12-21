from flask import request
from flask_restful import Resource
from ..Authenticator import Authenticator

class User(Resource):
    mysql = None

    @classmethod
    def setDatabase(self, param):
        self.mysql = param

    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        sql = '''SELECT * FROM users
            WHERE TX_USERNAME = %s 
            AND TX_PASSWORD = SHA2(%s, 256)'''

        cursor = self.mysql.connection.cursor()
        cursor.execute(sql, (username, password))
        data = cursor.fetchall()

        return data