from models.item import Item, ItemDAO

class View:
    @staticmethod
    def item_listar():
        return ItemDAO.listar()

    @staticmethod
    def item_inserir(nome, email, fone):
        cliente = Item(0, nome, email, fone)
        ItemDAO.inserir(cliente)
