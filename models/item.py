import sqlite3

class Item:
    def __init__(self, id: int | None, descricao: str, quantidade: int):
        self.id = id
        self.descricao = descricao
        self.quantidade = quantidade

    def __str__(self):
        pass    
        return f"Item(id={self.id}, descricao='{self.descricao}', quantidade={self.quantidade})"
    
    
class ItemDAO:
    def __init__(self, db_name="itens.db"):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def adicionar(self, item: Item):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
                       (item.descricao, item.quantidade))
        conn.commit()
        item.id = cursor.lastrowid
        conn.close()
        return item

    def listarTodos(self) -> list[Item]:
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens")
        rows = cursor.fetchall()
        conn.close()
        return [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in rows]