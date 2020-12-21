from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect, url_for
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import requests

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'liborg'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('user.html')
    else:
        return render_template('login.html')

@app.route('/list', methods=['GET'])
def list():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM books')
    result = cursor.fetchall()
    return render_template('list.html', books=result)


# called by regristration page to register user
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_passwd = request.form['user_password']
        cursor = mysql.get_db().cursor()
        cursor.execute("""INSERT INTO users (user_email,user_passwd) VALUES (%s,%s)""", (user_email, user_passwd))
        mysql.get_db().commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/user', methods=["POST"])
def user():
    return render_template('user.html')

@app.route("/bokksearch", methods="POST")
def booksearch():
    isbn = request.form['isbn']
    url = "https://robertalberto.com/" + isbn
    res = requests.get(url)
    scone = res.json()
    lst = scone['docs']
    for item in lst:
        isbn = item['isbn']
        title = item['title']
        author = item['author_name']
        lang = item['language']
        genre = item['subject']
        publisher = item['publisher']
    return render_template('list.html', isbn=isbn[0], title=title, author=author[0], lang=lang[0], genre=genre[0], publisher=publisher[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
