import tkinter as tk
from datetime import date, timedelta

from analytics import (
    today,
    current_streak,
    longest_streak,
    completion_percentage
)
from config import (
    BG, CARD, CARD2, WHITE, GRAY,
    BLUE, GREEN, RED, ORANGE
)
from storage import data
from ui import (
    main,
    selected_habit,
    create_button,
    clear_main
)
from actions import toggle_habit


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
            lambda n=name: toggle_habit(n, show_dashboard),
            RED if completed else GREEN
        ).pack(
            side="right",
            padx=10,
            pady=6
        )


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
            lambda n=name: toggle_habit(n, show_dashboard),
            RED if completed else GREEN
        ).pack(
            side="right",
            padx=5,
            pady=8
        )


def select_habit(name):

    selected_habit.set(name)

    show_history()


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
