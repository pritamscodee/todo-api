from sqllite3_db import get_connection

def create_task(task,is_completed):
           conn = get_connection()
           cur=conn.cursor()
           cur.execute("INSERT INTO todo(task,is_completed) VALUES(?,?)  ",(task,is_completed))
           id=cur.lastrowid
           conn.commit()
           return id 


def read_task():
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("SELECT * FROM todo")
        row = cur.fetchall()
        return row



def update_task(task,is_completed,id):
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("UPDATE todo SET task=?,is_completed=? WHERE id =? ",(task,is_completed,id))
        conn.commit()


def delete_task():
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM todo")
        conn.commit()
        