
from flask import Flask
from controllers.rotas import rotas
from database import criar_tabelas

app = Flask(__name__)
app.register_blueprint(rotas)

criar_tabelas()

if __name__ == "__main__":
    app.run(debug=True)
