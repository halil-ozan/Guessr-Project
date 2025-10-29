import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'game.db')
        self.create_tables()

    def create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            
            # Scores table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    score INTEGER,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            conn.commit()

    def add_user(self, username, password):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                             (username, password))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, username, password):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                         (username, password))
            return cursor.fetchone() is not None

    def save_score(self, username, score):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
            user_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO scores (user_id, score) VALUES (?, ?)', 
                         (user_id, score))
            conn.commit()

    def get_leaderboard(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT users.username, scores.score, scores.date
                FROM scores
                JOIN users ON users.id = scores.user_id
                ORDER BY scores.score DESC
                LIMIT 10
            ''')
            return cursor.fetchall()
