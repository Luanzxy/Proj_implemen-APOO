from typing import List

class ItemController:
    def __init__(self, dao: ItemDAO):
        self.dao = dao

    def criarItem(self, descricao: str, quantidade: int) -> Item:
        item = Item(id=None, descricao=descricao, quantidade=quantidade)
        return self.dao.adicionar(item)

    def obterTodosOsItens(self) -> List[Item]:
        return self.dao.listarTodos()
