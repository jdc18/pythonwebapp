from flask import Flask, redirect
from flask.ext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route("/")
def home():
    return redirect('/greetings')

@app.route("/greetings")
def greetings():
    return "Number of rows on db: ", 200

@app.route('/messages', methods=['POST'])
def messages():
    return "messages"

if __name__ == 'main':
   app.run()