from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql = MySQL(app)


app.config ['MYSQL_HOST'] = 'localhost'
app.config ['MYSQL_USER'] = 'root'
app.config ['MYSQL_PASSWORD'] = "123456"
app.config ['MYSQL_DB'] = 'order_management_system'

@app.route("/", methods = ['GET','POST']) 
def index():
    if request.method == 'POST':
        username= request.form['username']
        email= request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name,email) values (%s,%s)",(username,email))
        mysql.connection.commit()
        cur.close()
        return "Successfully updated Record in Database"
    return render_template('index.html')

@app.route("/users")
def getusers():
    cur = mysql.connection.cursor()
    user = cur.execute("SELECT * FROM users")
    if user >0:
        userDetails = cur.fetchall()
    return render_template('users.html', myuser=userDetails)

        
if __name__ == "__main__":
    app.run(debug=True)
        