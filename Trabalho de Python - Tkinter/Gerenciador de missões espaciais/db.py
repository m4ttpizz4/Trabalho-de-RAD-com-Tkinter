#bibliotecas:
import sqlite3

#conexao com o banco de dados:
def create_connection():
    conn = sqlite3.connect('missoes.db')
    return conn

#criaçao da tabela:
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS missao (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_lancamento DATE NOT NULL,
                        destino TEXT NOT NULL,
                        estado TEXT NOT NULL,
                        tripulacao TEXT NOT NULL,
                        carga_util TEXT NOT NULL,
                        duracao TEXT NOT NULL,
                        custo REAL NOT NULL,
                        status TEXT NOT NULL
                    )''')
    conn.commit()