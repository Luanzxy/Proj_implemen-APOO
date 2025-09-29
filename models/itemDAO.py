import sqlite3
from typing import List

class ItemDAO:
    def __init__(self, db_path="itens.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._criar_tabela()

    def _criar_tabela(self):
        query = """
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def adicionar(self, item: Item):
        query = "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (item.descricao, item.quantidade))
        self.conn.commit()
        item.id = cur.lastrowid  # Atualiza id do item com o gerado pelo banco
        return item

    def listarTodos(self) -> List[Item]:
        query = "SELECT id, descricao, quantidade FROM itens"
        cursor = self.conn.execute(query)
        itens = [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in cursor.fetchall()]
        return itens
