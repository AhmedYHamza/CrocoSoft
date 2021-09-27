from flask import Flask, request
from flaskext.mysql import MySQL
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "123456789"
app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
app.config['MYSQL_DATABASE_DB'] = "crocosoft"
app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

api = Api(app)


class addDoc(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO document(doc_id,is_from_outside,doc_status,date_created,date_modified)
        VALUES (%s,%s,%s,%s,%s)''', data)
        mysql.get_db().commit()
        return str(data)


api.add_resource(addDoc, '/add/doc')
