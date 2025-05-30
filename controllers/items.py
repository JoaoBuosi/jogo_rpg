# controllers/items.py

inventarios = {}

def adicionar_item(nome_usuario, item):
    if nome_usuario not in inventarios:
        inventarios[nome_usuario] = []
    inventarios[nome_usuario].append(item)

def listar_inventario(nome_usuario):
    return inventarios.get(nome_usuario, [])

def remover_item(nome_usuario, item):
    if nome_usuario in inventarios and item in inventarios[nome_usuario]:
        inventarios[nome_usuario].remove(item)
        return True
    return False
