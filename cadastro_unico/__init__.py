
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_PROIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from cadastro_unico.views import home ,login,agendar,cadastro_usuario,relatorio,comprovante
from cadastro_unico.models import Cadastro_usuario
