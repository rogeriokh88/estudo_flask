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

@app.route("/cadastro_usuario/")
def cadastro_usuario():
    return render_template("cadastro_usuario.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/relatorio/")
def relatorio():
    return render_template("relatorio.html")

@app.route("/comprovante/")
def comprovante():
    return render_template("comprovante_do_agendamento.html")