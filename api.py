from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

usuarios = []

DATA_FILE = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def salvar_usuarios():
    with open(DATA_FILE, 'w') as file:
        json.dump(usuarios, file, indent=4)

usuarios = carregar_usuarios()

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])        
def incluir_novo_usuario():
    novo_usuario = request.get_json()
    usuarios.append(novo_usuario)

    salvar_usuarios()

    return jsonify(usuarios), 201

app.run(port=5000, host='localhost', debug=True)
