
import sqlite3

def get_connection():
    return sqlite3.connect("eventpass.db")

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            capacidade_maxima INTEGER NOT NULL,
            local TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            evento_id INTEGER NOT NULL,
            FOREIGN KEY (evento_id) REFERENCES eventos(id)
        )
    """)

    conn.commit()
    conn.close()
