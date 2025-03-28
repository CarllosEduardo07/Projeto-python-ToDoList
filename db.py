import sqlite3 as sql



def init_db():
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        description TEXT,
                        status TEXT)""")    
    conn.commit()
    conn.close()
    
    
def create_task(title, description, status):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (title, description, status))
    conn.commit()
    conn.close()
    
def update_task(title, description, status, id):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?", (title, description, status, id))
    conn.commit()
    conn.close()


def read_task():
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    conn.close()
    return result


def delete_task(id):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()