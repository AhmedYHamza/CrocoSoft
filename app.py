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
        VALUES (%s,%s,%s,%s,%s)''', data[0:5])
        mysql.get_db().commit()
        if(data[1] == "1"):
            datasub = list(data[0])
            datasub.append(data[5])
            datasub.append(data[6])
            cursor.execute('''
            INSERT INTO outside_document(doc_id,receipt_date,receipt_num)
            VALUES (%s,%s,%s)''', datasub)
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
        if(results[0][1] == 1):
            cursor.execute('''
            SELECT *
            FROM outside_document
            WHERE outside_document.doc_id=%s''', doc_id)
            results = results + cursor.fetchall()[0][1:]
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


# Delete queries
class delDoc(Resource):
    def get(self, doc_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        SELECT is_from_outside
        FROM document
        WHERE document.doc_id=%s
        ''', doc_id)
        results = cursor.fetchall()
        if(results[0][0] == 1):
            cursor.execute('''
            DELETE
            FROM outside_document
            WHERE outside_document.doc_id=%s
            ''', doc_id)
            mysql.get_db().commit()
        cursor.execute('''
        DELETE
        FROM document
        WHERE document.doc_id=%s
        ''', doc_id)
        mysql.get_db().commit()
        return {}


class delDraft(Resource):
    def get(self, draft_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        DELETE
        FROM draft
        WHERE draft.draft_id=%s
        ''', draft_id)
        mysql.get_db().commit()
        return {}


class delCopy(Resource):
    def get(self, copy_id):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        DELETE
        FROM draft_copy
        WHERE draft_copy.copy_id=%s
        ''', copy_id)
        mysql.get_db().commit()
        return {}


class delEmp(Resource):
    def get(self, ssn):
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        DELETE
        FROM employee
        WHERE employee.ssn=%s
        ''', ssn)
        mysql.get_db().commit()
        return {}


# update queries
class updtDoc(Resource):
    def put(self, doc_id):
        data = list(request.form.values())
        datasub = list(data[0:5])
        datasub.append(doc_id)
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        UPDATE document 
        SET doc_id=%s,is_from_outside=%s,doc_status=%s,date_created=%s,date_modified=%s
        WHERE document.doc_id=%s''', datasub)
        mysql.get_db().commit()
        if(data[1] == "1"):
            datasub = list(data[0])
            datasub.append(data[5])
            datasub.append(data[6])
            datasub.append(doc_id)
            cursor.execute('''
            UPDATE outside_document
            SET doc_id=%s,receipt_date=%s,receipt_num=%s
            WHERE outside_document.doc_id=%s''', datasub)
            mysql.get_db().commit()
        return str(data)


class updtDraft(Resource):
    def put(self, draft_id):
        data = list(request.form.values())
        data.append(draft_id)
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        UPDATE draft
        SET draft_id=%s,doc_id=%s
        WHERE draft.draft_id=%s''', data)
        mysql.get_db().commit()
        return str(data)


class updtCopy(Resource):
    def put(self, copy_id):
        data = list(request.form.values())
        data.append(copy_id)
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        UPDATE draft_copy
        SET copy_id=%s,draft_id=%s
        WHERE draft_copy.copy_id=%s''', data)
        mysql.get_db().commit()
        return str(data)


class updtEmp(Resource):
    def put(self, ssn):
        data = list(request.form.values())
        data.append(ssn)
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        UPDATE employee
        ssn=%s,emp_name=%s,job_title=%s,email=%s
        WHERE employee.ssn=%s''', data)
        mysql.get_db().commit()
        return str(data)


# Transfer
class transDoc(Resource):
    def put(self):
        data = list(request.form.values())
        cursor = mysql.get_db().cursor()
        cursor.execute('''
        INSERT INTO document_circulation(circulation_id,source_id,source_type,emp_ssn,modify_date)
        VALUES (%s,%s,%s,%s,%s)''', data)
        mysql.get_db().commit()
        if(data[2] == "doc"):
            datasub = (str("Transfered to employee: " +
                       data[3]), data[4], data[1])
            print(datasub)
            cursor.execute('''
            UPDATE document
            SET doc_status=%s,date_modified=%s
            WHERE document.doc_id=%s''', datasub)
            mysql.get_db().commit()
        return str(data)


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

# Delete
api.add_resource(delDoc, '/del/doc/<int:doc_id>')
api.add_resource(delDraft, '/del/drft/<int:draft_id>')
api.add_resource(delCopy, '/del/cpy/<int:copy_id>')
api.add_resource(delEmp, '/del/emp/<int:ssn>')

# Update
api.add_resource(updtDoc, '/updt/doc/<int:doc_id>')
api.add_resource(updtDraft, '/updt/drft/<int:draft_id>')
api.add_resource(updtCopy, '/updt/cpy/<int:copy_id>')
api.add_resource(updtEmp, '/updt/emp/<int:ssn>')

# Transfer
api.add_resource(transDoc, '/transdoc')
