from cadastro_unico import db
from datetime import datetime , timezone

class Cadastro_usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=lambda:datetime.now(timezone.utc))
    nome = db.Column(db.String(100), nullable= True)
    sobrenome = db.Column(db.String(100), nullable=True)
    cpf = db.Column(db.String(11), nullable=True)
    data_nascimento = db.Column(db.String, nullable=True)