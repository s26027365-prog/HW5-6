tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
)
"""

read_tasks = """
    SELECT * FROM tasks
"""

update_tasks = """
    UPDATE tasks SET task = ? WHERE id = ?
"""

delete_tasks = """ 
    DELETE FROM tasks WHERE id = ?
"""


insert_tasks = """
    INSERT INTO tasks (task) VALUES (?)
"""