import sqlite3

def init_db():
    conn = sqlite3.connect("assignments.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT,
            pilot_id TEXT,
            drone_id TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_assignment(project_id, pilot_id, drone_id):
    init_db()
    conn = sqlite3.connect("assignments.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO assignments (project_id, pilot_id, drone_id) VALUES (?, ?, ?)",
        (project_id, pilot_id, drone_id)
    )
    conn.commit()
    conn.close()
