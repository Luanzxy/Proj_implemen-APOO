from models.item import Item
from models.item import ItemDAO

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, descricao: str, quantidade: int):
        item = Item(id=None, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self):
        return self.dao.listarTodos()
