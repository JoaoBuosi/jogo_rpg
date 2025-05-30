# controllers/auth.py

import json
import os

USUARIOS_PATH = "usuarios.json"

def carregar_usuarios():
    if not os.path.exists(USUARIOS_PATH):
        return []
    with open(USUARIOS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def salvar_usuarios(usuarios):
    with open(USUARIOS_PATH, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4)

def cadastrar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    if any(user['nome'] == nome for user in usuarios):
        return False  # Usuário já existe
    usuarios.append({"nome": nome, "senha": senha})
    salvar_usuarios(usuarios)
    return True

def autenticar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    return any(user['nome'] == nome and user['senha'] == senha for user in usuarios)
