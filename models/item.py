import sqlite3

class Item:
    def __init__(self, id, descricao, quantidade):
        self.id = id
        self.descricao = descricao
        self.quantidade = quantidade

class ItemDAO:
    def __init__(self, db_name="itens.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def adicionar(self, item: Item):
        self.cursor.execute(
            "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
            (item.descricao, item.quantidade)
        )
        self.conn.commit()

    def listarTodos(self):
        self.cursor.execute("SELECT id, descricao, quantidade FROM itens")
        rows = self.cursor.fetchall()
        return [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in rows]

    def remover(self, id_item: int) -> bool:
        self.cursor.execute("DELETE FROM itens WHERE id = ?", (id_item,))
        self.conn.commit()
        return self.cursor.rowcount > 0       