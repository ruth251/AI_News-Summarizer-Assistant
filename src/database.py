import sqlite3
from datetime import datetime

DB_NAME = "summarizer.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def setup_db():
    conn = get_connection()
    c = conn.cursor()

    # Create summaries table
    c.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT,
            source_content TEXT,
            summary TEXT,
            created_at TEXT
        )
    """)

    # Create questions table
    c.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            summary_id INTEGER,
            question TEXT,
            answer TEXT,
            asked_at TEXT,
            FOREIGN KEY (summary_id) REFERENCES summaries(id)
        )
    """)

    conn.commit()
    conn.close()

    
def save_summary(source_type, source_content, summary):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO summaries (source_type, source_content, summary, created_at)
        VALUES (?, ?, ?, ?)
    """, (source_type, source_content, summary, datetime.utcnow().isoformat()))

    conn.commit()
    summary_id = c.lastrowid
    conn.close()
    return summary_id

def save_question(summary_id, question, answer):
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO questions (summary_id, question, answer, asked_at)
        VALUES (?, ?, ?, ?)
    """, (summary_id, question, answer, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()
