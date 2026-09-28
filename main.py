import tkinter as tk

from config import CARD, GRAY
from ui import (
    root,
    sidebar,
    create_button
)
from actions import add_habit, delete_habit
from views import (
    show_dashboard,
    show_habits,
    show_history,
    show_about
)


tk.Label(
    sidebar,
    text="MENU",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=GRAY
).pack(
    anchor="w",
    padx=20,
    pady=(22, 10)
)


create_button(
    sidebar,
    "⌂  Dashboard",
    show_dashboard
).pack(
    fill="x",
    padx=12,
    pady=4
)


create_button(
    sidebar,
    "☷  My Habits",
    show_habits
).pack(
    fill="x",
    padx=12,
    pady=4
)


create_button(
    sidebar,
    "▣  History",
    show_history
).pack(
    fill="x",
    padx=12,
    pady=4
)


separator = tk.Frame(
    sidebar,
    bg="#303846",
    height=1
)

separator.pack(
    fill="x",
    padx=20,
    pady=18
)


create_button(
    sidebar,
    "+  Add Habit",
    lambda: add_habit(show_dashboard),
    "#35C98A"
).pack(
    fill="x",
    padx=12,
    pady=4
)


create_button(
    sidebar,
    "−  Delete Selected",
    lambda: delete_habit(show_dashboard),
    "#F05D72"
).pack(
    fill="x",
    padx=12,
    pady=4
)


create_button(
    sidebar,
    "ⓘ  About",
    show_about
).pack(
    fill="x",
    padx=12,
    pady=4
)


tk.Label(
    sidebar,
    text="Data saves automatically",
    font=("Arial", 8),
    bg=CARD,
    fg=GRAY
).pack(
    side="bottom",
    pady=15
)


show_dashboard()

root.mainloop()
