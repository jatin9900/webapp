from flask import Flask, render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.cizf7nvnlpgd.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Seema1996",
  database="mydatabase"
)

helloworld = Flask(__name__)

@helloworld.route("/<code>")
def error(code):
    if code=='404':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT * FROM errorcode WHERE code ='404';")
        result = mycursor1.fetchone()
        return render_template("index.html", result = result)

    if code=='403':
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM errorcode WHERE code ='403';")
        result = mycursor2.fetchone()
        return render_template("index.html", result = result)

    if code=='500':
        mycursor3 = mydb.cursor()
        mycursor3.execute("SELECT * FROM errorcode WHERE code ='500'")
        result = mycursor3.fetchone()
        return render_template("index.html", result = result)

    if code=='502':
        mycursor4 = mydb.cursor()
        mycursor4.execute("SELECT value FROM errorcode WHERE code ='502'")
        result = mycursor4.fetchone() 
        return render_template("index.html", result = result)


if __name__=="__main__":
    helloworld.run(host="0.0.0.0",port=int("5000"),debug="True")