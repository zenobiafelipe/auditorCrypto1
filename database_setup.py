import sqlite3

def setup_database():
    conn = sqlite3.connect('auditor_app.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Insertar un usuario por defecto
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', ('admin', 'password123'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
