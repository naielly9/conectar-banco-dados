import sqlite3

class Database:
    def __init__(self, db_name='aula.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    def add_user(self, username, email, password):
        self.cursor.execute("INSERT INTO users(username, email, password) VALUES (?,?,?)",(username, email, password))
        self.conn.commit()
        
    def close(self):
        self.conn.close()