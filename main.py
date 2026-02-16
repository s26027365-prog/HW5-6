from db import main_db 
import flet as ft 


def main(page: ft.Page):
    tasks_column = ft.Column()

    def add_new_task(e):
        def delete_from_db(id):
            main_db.delete_task(id)
    
        def edit_db(id, new_value):
            main_db.edit_task(id, new_value)
            print("Задача обновлена")

        def edit(e):
            task_text.read_only = True
            edit_db(task_id, task_text.value)

        def delete(e):
            tasks_column.controls.remove(task_row)
            delete_from_db(task_id)

        def add_to_db(name):
            id = main_db.add_new_task(name)
            print("добавлена новая задача: {name} ID: {id}")
            return id

        def to_edit(e):
            if task_text.read_only:
                task_text.read_only = False
            else:
                task_text.read_only = True

        if user_input.value:
            task_text = ft.TextField(
                value=user_input.value, expand=True, read_only=True, on_submit=edit
            )
            task_text = ft.TextField(value=user_input.value, expand=True, read_only=True)
            submin_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=edit)
            delete_button = ft.IconButton(icon=ft.Icons.DELETE,icon_color=ft.Colors.RED, on_click=delete)
            edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit)
            task_id = add_to_db(user_input.value)
            user_input.value = None
            task_row = ft.Row([task_text, edit_button, submin_button, delete_button])
            tasks_column.controls.append(task_row)
    

    user_input = ft.TextField(label="новая задача", expand=True)
    enter_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)

    main_row = ft.Row([user_input, enter_button])

    page.add(main_row, tasks_column)
    


if __name__=="__main__":
    main_db.create_tables()
    ft.run(main)