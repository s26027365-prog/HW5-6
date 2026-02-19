import flet as ft
from db import main_db


def main(page: ft.Page):
    tasks_collumn = ft.Column(spacing=5)

    def load_from_db():
        tasks_collumn.controls.clear()
        results = main_db.get_all_tasks()

        if results:
            for task_id, task, completed in results:
                tasks_collumn.controls.append(
                    add_task(task_id, task, completed)
                )
        page.update()

    def add_task(task_id, task, completed):

        def edit(e):
            main_db.edit_task(task_id, task_text.value)
            task_text.read_only = True
            page.update()

        def delete(e):
            main_db.delete_task(task_id)
            tasks_collumn.controls.remove(task_row)
            page.update()

        def to_edit(e):
            task_text.read_only = not task_text.read_only
            page.update()

        def change_completed(e):
            main_db.set_completed(task_id, checkbox.value)

        checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=change_completed
        )

        task_text = ft.TextField(
            value=task,
            expand=True,
            read_only=True,
            on_submit=edit
        )

        task_row = ft.Row([
            checkbox,
            task_text,
            ft.IconButton(icon=ft.Icons.EDIT, on_click=to_edit),
            ft.IconButton(icon=ft.Icons.SAVE, on_click=edit),
            ft.IconButton(icon=ft.Icons.DELETE, on_click=delete),
        ])

        return task_row

    def add_new_task(e):
        if user_input.value:
            task_id = main_db.add_new_task(user_input.value)
            tasks_collumn.controls.append(
                add_task(task_id, user_input.value, 0)
            )
            user_input.value = ""
            page.update()

    def clear_completed(e):
        main_db.delete_completed_tasks()
        load_from_db()

    user_input = ft.TextField(
        label="Новая задача",
        expand=True,
        on_submit=add_new_task
    )

    page.add(
        ft.Row([
            user_input,
            ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_task)
        ]),
        ft.ElevatedButton("Очистить выполненные", on_click=clear_completed),
        tasks_collumn
    )

    load_from_db()


if __name__ == "__main__":
    main_db.create_tables()
    ft.run(main, view=ft.AppView.WEB_BROWSER)
