import tkinter as tk
from tkinter import messagebox, simpledialog

from analytics import today
from storage import data, save_data
from ui import root, selected_habit


def add_habit(refresh):

    name = simpledialog.askstring(
        "Add Habit",
        "Enter your new habit:",
        parent=root
    )

    if name is None:
        return

    name = name.strip()

    if not name:
        messagebox.showwarning(
            "Invalid Habit",
            "Habit name cannot be empty."
        )
        return

    if name in data["habits"]:

        messagebox.showwarning(
            "Already Exists",
            "This habit already exists."
        )

        return

    data["habits"][name] = {
        "created": today(),
        "completed": []
    }

    save_data()
    refresh()


def delete_habit(refresh):

    name = selected_habit.get()

    if not name or name not in data["habits"]:

        messagebox.showinfo(
            "Select Habit",
            "First select a habit from My Habits."
        )

        return

    confirm = messagebox.askyesno(
        "Delete Habit",
        f"Are you sure you want to delete '{name}'?"
    )

    if confirm:

        del data["habits"][name]

        selected_habit.set("")

        save_data()
        refresh()


def toggle_habit(name, refresh):

    habit = data["habits"][name]

    current_date = today()

    if current_date in habit["completed"]:

        habit["completed"].remove(current_date)

    else:

        habit["completed"].append(current_date)

    save_data()
    refresh()
