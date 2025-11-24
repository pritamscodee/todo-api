import sqlite3

def get_connection():
    conn = sqlite3.connect('todo.db')
   
    return conn

def creating_table():
    con=get_connection()
    cur=con.cursor()
    cur.execute("""
CREATE TABLE IF NOT EXISTS todo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                is_completed BOOLEAN
                
                )
                """)


creating_table()