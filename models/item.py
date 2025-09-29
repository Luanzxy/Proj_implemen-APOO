class Item:
    def __init__(self, id: int, descricao: str, quantidade: int):
        self.id = id
        self.descricao = descricao
        self.quantidade = quantidade

    def __repr__(self):
        return f"Item(id={self.id}, descricao='{self.descricao}', quantidade={self.quantidade})"