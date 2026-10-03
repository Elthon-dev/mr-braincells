"""Persistent memory system"""
import sqlite3
import os
from datetime import datetime

class MemoryManager:
    def __init__(self, db_path: str = None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "..", "..", "memory.db")
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS memories
                     (id INTEGER PRIMARY KEY, content TEXT, timestamp TEXT, importance REAL)''')
        conn.commit()
        conn.close()

    def add(self, content: str, importance: float = 0.5):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO memories (content, timestamp, importance) VALUES (?, ?, ?)",
                  (content, datetime.now().isoformat(), importance))
        conn.commit()
        conn.close()
