from cadastro_unico import app
from flask import render_template,url_for

@app.route("/")
def home():
    
    context = {
        "usuario" : "rogerio",
        "idade" : 32 

        }
    return render_template("index.html")

@app.route("/agendar/")
def agendar():
    return render_template("agendar.html")

@app.route("/cadastro/")
def cadastro():
    return render_template("cadastro.html")

@app.route("/login/")
def login():
    return render_template("login.html")