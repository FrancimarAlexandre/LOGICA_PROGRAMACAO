import sqlite3

class BD_estacionamento():
    def connect(self):
        self.conn = sqlite3.connect("estacionamento.db")
        self.cursor = self.conn.cursor()
        
    def desconect(self):
        self.cursor.close()
    
    def create_table(self):
        self.connect()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS estacionamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                proprietario TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                placa TEXT NOT NULL
            )
        """)
        self.conn.commit()  
        self.desconect()
        
# test = BD_estacionamento()
# test.create_table()