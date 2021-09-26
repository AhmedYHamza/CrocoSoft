from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = "dvddisc1A@"
app.config['MYSQL_DATABASE_HOST'] = "127.0.0.1"
app.config['MYSQL_DATABASE_DB'] = "crocosoft"
app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    cursor = mysql.get_db().cursor()

    cursor.execute('''
    SELECT* 
    FROM Document;''')
    results = cursor.fetchall()
    print(results)
    return str(results)
