tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL ,
        completed INTEGER DEFAULT 0
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

add_completed_column = """
ALTER TABLE tasks ADD COLUMN completed INTEGER DEFAULT 0
"""

delete_completed = """
DELETE FROM tasks WHERE completed = 1
"""

set_completed = """
UPDATE tasks SET completed = ? WHERE id = ?
"""


