import tkinter as tk

tasks = []
completed_tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    update_task_list()
    save_tasks_to_file("tasks.txt")
    task_entry.delete(0, tk.END)

def view_tasks():
    update_task_list()

def complete_task(task_index):
    if 0 <= task_index < len(tasks) and not tasks[task_index]["completed"]:
        tasks[task_index]["completed"] = True
        completed_tasks.append(tasks[task_index])
        tasks.pop(task_index)
        update_task_list()
        save_tasks_to_file("tasks.txt")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        update_task_list()
        save_tasks_to_file("tasks.txt")

def edit_task(task_index, new_task):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["task"] = new_task
        update_task_list()
        save_tasks_to_file("tasks.txt")

def save_tasks_to_file(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")

def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        if not task["completed"]:
            task_list.insert(tk.END, f"{i + 1}. {task['task']}")

def add_task_button_click():
    task = task_entry.get()
    if task:
        add_task(task)

def edit_task_button_click():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        new_task = task_entry.get()
        edit_task(task_index, new_task)

def delete_task_button_click():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        delete_task(task_index)

def complete_task_button_click():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        complete_task(task_index)

def load_tasks_from_file(filename):
    tasks.clear()
    try:
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                if len(task_data) == 2:
                    task, completed = task_data
                    tasks.append({"task": task, "completed": completed == "True"})
    except FileNotFoundError:
        pass

load_tasks_from_file("tasks.txt")

root = tk.Tk()
root.title("Aplikasi Daftar Tugas")

task_list = tk.Listbox(root)
task_list.pack()

task_entry = tk.Entry(root)
task_entry.pack()

add_task_button = tk.Button(root, text="Tambah Tugas", command=add_task_button_click)
add_task_button.pack()

edit_task_button = tk.Button(root, text="Edit Tugas", command=edit_task_button_click)
edit_task_button.pack()

delete_task_button = tk.Button(root, text="Hapus Tugas", command=delete_task_button_click)
delete_task_button.pack()

complete_task_button = tk.Button(root, text="Selesaikan Tugas", command=complete_task_button_click)
complete_task_button.pack()

update_task_list()

root.mainloop()
