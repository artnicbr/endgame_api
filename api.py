from flask import Flask
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from .routes import Routes

#API CONFIGS AND DEFINITIONS
app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = '192.168.56.4'
app.config['MYSQL_USER'] = 'andre'
app.config['MYSQL_PASSWORD'] = 'andre'
app.config['MYSQL_DB'] = 'endgameapp'

mysql = MySQL(app)

Routes.setRoutes(api, mysql)

if __name__ == '__main__':
    app.run(debug=True)