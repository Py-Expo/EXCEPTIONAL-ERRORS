from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dhanu@9090@#$'
app.config['MYSQL_DB'] = 'Minvazhi thoodhu'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('signin.html')

@app.route('/homepage.html', methods=['POST', 'GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/signuppage.html', methods=['GET', 'POST'])
def signup():
    return render_template('signuppage.html')

@app.route('/event.html', methods=['POST', 'GET'])
def event():
    return render_template('event.html')

@app.route('/editprofile.html', methods=['POST', 'GET'])
def editprofile():
    return render_template('editprofile.html')

@app.route('/test_mysql_connection')
def test_mysql_connection():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        cursor.close()
        return f"MySQL Server Version: {data[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
