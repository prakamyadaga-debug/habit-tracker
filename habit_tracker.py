import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import date, timedelta
import json
from pathlib import Path

# ============================================================
# HABIT TRACKER
# Single-file Python project
# ============================================================

DATA_FILE = Path("habits.json")

# ---------------- DATA HANDLING ----------------

def load_data():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            pass

    return {"habits": {}}


data = load_data()


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def today():
    return date.today().isoformat()


# ---------------- HABIT CALCULATIONS ----------------

def current_streak(completed_dates):
    dates = set(completed_dates)
    current = date.today()
    streak = 0

    while current.isoformat() in dates:
        streak += 1
        current -= timedelta(days=1)

    return streak


def longest_streak(completed_dates):
    if not completed_dates:
        return 0

    dates = sorted(
        date.fromisoformat(d)
        for d in set(completed_dates)
    )

    longest = 1
    streak = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            streak += 1
            longest = max(longest, streak)
        else:
            streak = 1

    return longest


def completion_percentage(habit):
    start = date.fromisoformat(habit["created"])
    days = (date.today() - start).days + 1

    completed = 0

    for d in habit["completed"]:
        completed_date = date.fromisoformat(d)

        if start <= completed_date <= date.today():
            completed += 1

    if days <= 0:
        return 0

    return round((completed / days) * 100)


# ---------------- COLORS ----------------

BG = "#10141C"
CARD = "#1A202B"
CARD2 = "#232B38"

WHITE = "#F5F7FA"
GRAY = "#AAB2BF"

BLUE = "#5B7CFA"
GREEN = "#35C98A"
RED = "#F05D72"
ORANGE = "#F5A742"


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Habit Tracker")
root.geometry("950x650")
root.minsize(800, 550)

root.configure(bg=BG)


# ---------------- HEADER ----------------

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


# ---------------- MAIN LAYOUT ----------------

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


# ---------------- BUTTON FUNCTION ----------------

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


# ---------------- CLEAR MAIN ----------------

def clear_main():

    for widget in main.winfo_children():
        widget.destroy()


# ============================================================
# DASHBOARD
# ============================================================

def show_dashboard():

    clear_main()

    habits = list(data["habits"].values())

    total = len(habits)

    completed_today = sum(
        1
        for habit in habits
        if today() in habit["completed"]
    )

    if total:
        overall_progress = round(
            sum(
                completion_percentage(h)
                for h in habits
            ) / total
        )
    else:
        overall_progress = 0

    best_streak = max(
        (
            longest_streak(h["completed"])
            for h in habits
        ),
        default=0
    )

    tk.Label(
        main,
        text="Dashboard",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(
        anchor="w",
        pady=(0, 15)
    )


    # -------- STAT CARDS --------

    stats = tk.Frame(main, bg=BG)
    stats.pack(fill="x")


    cards = [
        ("Total Habits", str(total), BLUE),
        ("Completed Today", f"{completed_today}/{total}", GREEN),
        ("Overall Progress", f"{overall_progress}%", "#9B6CFF"),
        ("Best Streak", f"{best_streak} days", ORANGE)
    ]


    for label, value, color in cards:

        card = tk.Frame(
            stats,
            bg=CARD,
            height=105
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        card.pack_propagate(False)


        tk.Label(
            card,
            text=label,
            font=("Arial", 10),
            bg=CARD,
            fg=GRAY
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 3)
        )


        tk.Label(
            card,
            text=value,
            font=("Arial", 22, "bold"),
            bg=CARD,
            fg=color
        ).pack(
            anchor="w",
            padx=15
        )


    # -------- TODAY'S HABITS --------

    section = tk.Frame(
        main,
        bg=CARD
    )

    section.pack(
        fill="both",
        expand=True,
        pady=20
    )


    tk.Label(
        section,
        text="Today's Habits",
        font=("Arial", 15, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(
        anchor="w",
        padx=20,
        pady=(18, 10)
    )


    if not habits:

        tk.Label(
            section,
            text="No habits yet.\n\nClick '+ Add Habit' to create your first habit.",
            font=("Arial", 12),
            bg=CARD,
            fg=GRAY,
            justify="center"
        ).pack(expand=True)

        return


    for name, habit in data["habits"].items():

        completed = today() in habit["completed"]

        row = tk.Frame(
            section,
            bg=CARD2
        )

        row.pack(
            fill="x",
            padx=15,
            pady=5
        )


        tk.Label(
            row,
            text=("✓  " if completed else "○  ") + name,
            font=("Arial", 11, "bold"),
            bg=CARD2,
            fg=GREEN if completed else WHITE
        ).pack(
            side="left",
            padx=15,
            pady=11
        )


        tk.Label(
            row,
            text=f"🔥 {current_streak(habit['completed'])} day streak",
            font=("Arial", 9),
            bg=CARD2,
            fg=GRAY
        ).pack(side="left")


        create_button(
            row,
            "Undo" if completed else "Mark Done",
            lambda n=name: toggle_habit(n),
            RED if completed else GREEN
        ).pack(
            side="right",
            padx=10,
            pady=6
        )


# ============================================================
# ADD HABIT
# ============================================================

def add_habit():

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

    show_dashboard()


# ============================================================
# DELETE HABIT
# ============================================================

def delete_habit():

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

        show_dashboard()


# ============================================================
# MARK HABIT DONE / UNDO
# ============================================================

def toggle_habit(name):

    habit = data["habits"][name]

    current_date = today()


    if current_date in habit["completed"]:

        habit["completed"].remove(current_date)

    else:

        habit["completed"].append(current_date)


    save_data()

    show_dashboard()


# ============================================================
# MY HABITS
# ============================================================

def show_habits():

    clear_main()


    tk.Label(
        main,
        text="My Habits",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(
        anchor="w",
        pady=(0, 15)
    )


    if not data["habits"]:

        tk.Label(
            main,
            text="No habits added yet.",
            font=("Arial", 13),
            bg=BG,
            fg=GRAY
        ).pack(pady=60)

        return


    for name, habit in data["habits"].items():

        card = tk.Frame(
            main,
            bg=CARD
        )

        card.pack(
            fill="x",
            pady=6
        )


        tk.Label(
            card,
            text=name,
            font=("Arial", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(
            side="left",
            padx=18,
            pady=15
        )


        tk.Label(
            card,
            text=f"🔥 {current_streak(habit['completed'])} days",
            bg=CARD,
            fg=GREEN
        ).pack(
            side="left",
            padx=10
        )


        tk.Label(
            card,
            text=f"Progress: {completion_percentage(habit)}%",
            bg=CARD,
            fg=GRAY
        ).pack(
            side="left",
            padx=10
        )


        create_button(
            card,
            "Select",
            lambda n=name: select_habit(n),
            BLUE
        ).pack(
            side="right",
            padx=5,
            pady=8
        )


        completed = today() in habit["completed"]


        create_button(
            card,
            "Done" if completed else "Mark Done",
            lambda n=name: toggle_habit(n),
            RED if completed else GREEN
        ).pack(
            side="right",
            padx=5,
            pady=8
        )


# ============================================================
# SELECT HABIT
# ============================================================

selected_habit = tk.StringVar()


def select_habit(name):

    selected_habit.set(name)

    show_history()


# ============================================================
# HISTORY
# ============================================================

def show_history():

    clear_main()


    name = selected_habit.get()


    tk.Label(
        main,
        text="Habit History",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(
        anchor="w",
        pady=(0, 5)
    )


    if not name or name not in data["habits"]:

        tk.Label(
            main,
            text="Select a habit from My Habits first.",
            font=("Arial", 12),
            bg=BG,
            fg=GRAY
        ).pack(
            anchor="w",
            pady=20
        )

        return


    habit = data["habits"][name]


    # -------- SUMMARY --------

    summary = tk.Frame(
        main,
        bg=CARD
    )

    summary.pack(
        fill="x",
        pady=15
    )


    metrics = [
        ("Habit", name),
        ("Current Streak",
         f"{current_streak(habit['completed'])} days"),
        ("Longest Streak",
         f"{longest_streak(habit['completed'])} days"),
        ("Completion",
         f"{completion_percentage(habit)}%")
    ]


    for label, value in metrics:

        box = tk.Frame(
            summary,
            bg=CARD
        )

        box.pack(
            side="left",
            expand=True,
            fill="x",
            pady=15
        )


        tk.Label(
            box,
            text=label,
            bg=CARD,
            fg=GRAY,
            font=("Arial", 9)
        ).pack()


        tk.Label(
            box,
            text=value,
            bg=CARD,
            fg=WHITE,
            font=("Arial", 12, "bold")
        ).pack(pady=4)


    # -------- LAST 30 DAYS --------

    history = tk.Frame(
        main,
        bg=CARD
    )

    history.pack(
        fill="both",
        expand=True
    )


    tk.Label(
        history,
        text="Last 30 Days",
        font=("Arial", 14, "bold"),
        bg=CARD,
        fg=WHITE
    ).pack(
        anchor="w",
        padx=20,
        pady=15
    )


    for i in range(29, -1, -1):

        current_date = date.today() - timedelta(days=i)

        date_text = current_date.isoformat()

        completed = date_text in habit["completed"]


        row = tk.Frame(
            history,
            bg=CARD2
        )

        row.pack(
            fill="x",
            padx=15,
            pady=2
        )


        tk.Label(
            row,
            text=current_date.strftime(
                "%a, %d %b %Y"
            ),
            bg=CARD2,
            fg=WHITE,
            font=("Arial", 10)
        ).pack(
            side="left",
            padx=12,
            pady=6
        )


        tk.Label(
            row,
            text="✓ Completed"
            if completed
            else "— Not completed",
            bg=CARD2,
            fg=GREEN if completed else GRAY,
            font=("Arial", 10, "bold")
        ).pack(
            side="right",
            padx=12
        )


# ============================================================
# ABOUT
# ============================================================

def show_about():

    clear_main()


    tk.Label(
        main,
        text="About the Project",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(
        anchor="w",
        pady=(0, 20)
    )


    card = tk.Frame(
        main,
        bg=CARD
    )

    card.pack(
        fill="x"
    )


    text = """
Habit Tracker

A simple desktop productivity application
created using Python and Tkinter.

Features:
• Add and delete habits
• Mark habits as completed
• Daily progress tracking
• Current streak calculation
• Longest streak calculation
• Completion percentage
• 30-day history
• Automatic JSON data storage
• Dashboard statistics

Python concepts used:
• Functions
• Lists
• Dictionaries
• Loops
• Conditional statements
• File handling
• JSON
• Date and time
• GUI event handling
• CRUD operations
"""


    tk.Label(
        card,
        text=text,
        font=("Arial", 11),
        bg=CARD,
        fg=WHITE,
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=30
    )


# ============================================================
# SIDEBAR
# ============================================================

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
    add_habit,
    GREEN
).pack(
    fill="x",
    padx=12,
    pady=4
)


create_button(
    sidebar,
    "−  Delete Selected",
    delete_habit,
    RED
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


# ============================================================
# START APPLICATION
# ============================================================

show_dashboard()

root.mainloop()