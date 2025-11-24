import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            tasks = json.load(f)
            for t in tasks:
                listbox.insert(tk.END, t)

def save_tasks():
    tasks = list(listbox.get(0, tk.END))
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

app = tk.Tk()
app.title("To-Do List App")
app.geometry("300x420")

listbox = tk.Listbox(app, width=40, height=15)
listbox.pack(pady=20)

entry = tk.Entry(app, width=30)
entry.pack()

add_btn = tk.Button(app, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(app, text="Delete Selected Task", command=delete_task)
delete_btn.pack()

load_tasks()
app.mainloop()
