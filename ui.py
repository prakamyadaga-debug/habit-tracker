import tkinter as tk
from datetime import date

from config import (
    BG, CARD, CARD2, WHITE, GRAY,
    BLUE, GREEN, RED, ORANGE
)


root = tk.Tk()

root.title("Habit Tracker")
root.geometry("950x650")
root.minsize(800, 550)
root.configure(bg=BG)


header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=25, pady=(20, 10))


title = tk.Label(
    header,
    text="Habit Tracker",
    font=("Arial", 26, "bold"),
    bg=BG,
    fg=WHITE
)

title.pack(side="left")


date_label = tk.Label(
    header,
    text="",
    font=("Arial", 11),
    bg=BG,
    fg=GRAY
)

date_label.pack(side="right")


def update_date():
    date_label.config(
        text=date.today().strftime("%A, %d %B %Y")
    )

    root.after(60000, update_date)


update_date()


content = tk.Frame(root, bg=BG)
content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)


sidebar = tk.Frame(
    content,
    bg=CARD,
    width=220
)

sidebar.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

sidebar.pack_propagate(False)


main = tk.Frame(
    content,
    bg=BG
)

main.pack(
    side="right",
    fill="both",
    expand=True
)


selected_habit = tk.StringVar()


def create_button(parent, text, command, color=BLUE):

    return tk.Button(
        parent,
        text=text,
        command=command,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=10,
        pady=9
    )


def clear_main():

    for widget in main.winfo_children():
        widget.destroy()
