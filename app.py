from flask import Flask , render_template, url_for, redirect, request
import sqlite3
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")



if __name__=="__main__":
    app.run(debug=True)
