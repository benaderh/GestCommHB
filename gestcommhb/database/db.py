import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'gestcommhb.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    # Création des tables principales
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference TEXT UNIQUE NOT NULL,
        designation TEXT NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0,
        pmp REAL NOT NULL DEFAULT 0.0
    );
    CREATE TABLE IF NOT EXISTS achats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        article_id INTEGER NOT NULL,
        quantite INTEGER NOT NULL,
        prix_unitaire REAL NOT NULL,
        FOREIGN KEY(article_id) REFERENCES articles(id)
    );
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        article_id INTEGER NOT NULL,
        quantite INTEGER NOT NULL,
        prix_unitaire REAL NOT NULL,
        FOREIGN KEY(article_id) REFERENCES articles(id)
    );
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
