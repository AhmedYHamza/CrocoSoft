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

# Add queries


class addDoc(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO document(doc_id,is_from_outside,doc_status,date_created,date_modified)
        VALUES (%s,%s,%s,%s,%s)''', data)
        mysql.get_db().commit()
        return str(data)


class addDraft(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO draft(draft_id,doc_id)
        VALUES (%s,%s)''', data)
        mysql.get_db().commit()
        return str(data)


class addCopy(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO draft_copy(copy_id,draft_id)
        VALUES (%s,%s)''', data)
        mysql.get_db().commit()
        return str(data)


class addEmp(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO employee(ssn,emp_name,job_title,email)
        VALUES (%s,%s,%s,%s)''', data)
        mysql.get_db().commit()
        return str(data)


# get queries
class getDoc(Resource):
    def get(self, doc_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        SELECT *
        FROM document
        WHERE document.doc_id=%s
        ''', doc_id)
        results = cursor.fetchall()
        print(results)
        return str(results)


class getDraft(Resource):
    def get(self, draft_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        SELECT *
        FROM draft
        WHERE draft.draft_id=%s
        ''', draft_id)
        results = cursor.fetchall()
        print(results)
        return str(results)


class getCopy(Resource):
    def get(self, copy_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        SELECT *
        FROM draft_copy
        WHERE draft_copy.copy_id=%s
        ''', copy_id)
        results = cursor.fetchall()
        print(results)
        return str(results)


class getEmp(Resource):
    def get(self, ssn):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        SELECT *
        FROM employee
        WHERE employee.ssn=%s
        ''', ssn)
        results = cursor.fetchall()
        print(results)
        return str(results)


# Add
api.add_resource(addDoc, '/add/doc')
api.add_resource(addDraft, '/add/drft')
api.add_resource(addCopy, '/add/cpy')
api.add_resource(addEmp, '/add/emp')

# Get
api.add_resource(getDoc, '/get/doc/<int:doc_id>')
api.add_resource(getDraft, '/get/drft/<int:draft_id>')
api.add_resource(getCopy, '/get/cpy/<int:copy_id>')
api.add_resource(getEmp, '/get/emp/<int:ssn>')
