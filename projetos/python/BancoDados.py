import sqlite3

class BD_estacionamento():
    def __init__(self):
        self.create_table()
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
    
    def insert(self,proprietario,marca,modelo,placa):
        self.connect()
        self.cursor.execute("""
            INSERT INTO estacionamento(proprietario,marca,modelo,placa)
            VALUES(?,?,?,?)
                            """,(proprietario,marca,modelo,placa))
        self.conn.commit()
        self.desconect()
# test = BD_estacionamento()
# test.create_table()