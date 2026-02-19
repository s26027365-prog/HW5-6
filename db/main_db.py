import config 
import sqlite3
from db import queries

def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.tasks_table)

    conn.commit()
    conn.close()

def add_new_task(name):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.insert_tasks, (name,))

    conn.commit()
    conn.close()

    id = cursor.lastrowid

    return id

def edit_task(id, new_value):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.update_tasks, (new_value, id))

    conn.commit()
    conn.close()

def delete_task(id):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_tasks, (id,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.read_tasks)
    result = cursor.fetchall()
    conn.close()
    return result

def set_completed(task_id, completed):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(
        queries.set_completed,
        (1 if completed else 0, task_id)
    )

    conn.commit()
    conn.close()

def delete_completed_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_completed)

    conn.commit()
    conn.close()



    
