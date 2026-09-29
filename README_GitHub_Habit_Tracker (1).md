# Habit Tracker

## Project Overview

**Habit Tracker** is a Python-based desktop application designed to help users create, manage, and track their daily habits.

The application allows users to add, edit, delete, and complete habits while maintaining completion history. It also calculates current and longest streaks and provides basic statistics to help users monitor their consistency.

The project uses a simple graphical user interface and stores data locally using a JSON file.

---

## Features

- Add new habits
- Edit existing habits
- Delete habits
- Add habit descriptions
- Mark habits as completed
- Undo habit completion
- Track completion history
- Calculate current streaks
- Calculate longest streaks
- Display today's completion percentage
- Display total habits
- Display completed habits for today
- View seven-day statistics
- View habit-wise performance
- Store data permanently in JSON
- Input validation
- Duplicate habit prevention
- User-friendly graphical interface

---

## Technologies / Tools Used

- **Python 3.10+**
- **Tkinter** – Graphical User Interface
- **JSON** – Local data storage
- **VS Code** – Development environment
- **Git & GitHub** – Version control and project repository

### Python Libraries

The project uses Python's built-in libraries:

- `tkinter`
- `datetime`
- `json`
- `pathlib`
- `dataclasses`
- `typing`

**No external Python packages are required.**

---

## Project Structure

```text
HabitTracker/
│
├── main.py
├── config.py
├── models.py
├── storage.py
├── habit_manager.py
├── analytics.py
├── validators.py
├── ui.py
├── utils.py
│
├── data/
│   └── habits.json
│
├── screenshots/
│
├── README.md
├── statement.md
└── requirements.txt
```

### File Description

| File | Description |
|---|---|
| `main.py` | Starts the application |
| `config.py` | Contains application configuration |
| `models.py` | Defines the Habit data model |
| `storage.py` | Handles JSON data storage |
| `habit_manager.py` | Handles habit operations |
| `analytics.py` | Calculates statistics and streaks |
| `validators.py` | Validates user input |
| `ui.py` | Creates the Tkinter GUI |
| `utils.py` | Contains date and utility functions |
| `habits.json` | Stores habit data |

---

# Installation & Run

## 1. Install Python

Install **Python 3.10 or later**.

Check the installed version:

```bash
python --version
```

## 2. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Then:

```bash
cd HabitTracker
```

## 3. Open in VS Code

Open the `HabitTracker` folder in Visual Studio Code.

## 4. Run the Application

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

The Habit Tracker application will open.

---

# How to Use

### Add a Habit

1. Click **Add Habit**.
2. Enter the habit name.
3. Enter an optional description.
4. Click **Save**.

### Edit a Habit

1. Select a habit.
2. Click **Edit Habit**.
3. Update the information.
4. Click **Save**.

### Complete a Habit

1. Select a habit.
2. Click **Mark Complete / Undo**.
3. The habit will be marked as completed for the current day.

### Undo Completion

Select the completed habit and click **Mark Complete / Undo** again.

### Delete a Habit

1. Select a habit.
2. Click **Delete Habit**.
3. Confirm the deletion.

### View Statistics

Click **Statistics** to view:

- Total completions
- Seven-day completion data
- Completion percentage
- Current streak
- Longest streak
- Habit-wise performance

---

# Testing Instructions

| Test Case | Action | Expected Result |
|---|---|---|
| Add Habit | Add a valid habit | Habit appears in the list |
| Edit Habit | Edit an existing habit | Updated information is displayed |
| Delete Habit | Delete a selected habit | Habit is removed |
| Complete Habit | Mark a habit complete | Status changes to `✓ Done` |
| Undo Completion | Mark completed habit again | Status changes to `Pending` |
| Empty Name | Try saving without a name | Validation message appears |
| Duplicate Habit | Add an existing habit name | Duplicate is rejected |
| Persistence | Close and reopen application | Saved data remains available |
| Statistics | Open Statistics | Statistics are displayed |
| Streak | Complete habits on consecutive days | Streak is calculated |

---

# Data Storage

The application stores data locally in:

```text
data/habits.json
```

The JSON file contains:

- Habit ID
- Habit name
- Description
- Creation date
- Completion dates

Example:

```json
[
    {
        "habit_id": 1,
        "name": "Study Python",
        "description": "Practice Python programming",
        "created_date": "2026-09-29",
        "completed_dates": [
            "2026-09-29"
        ]
    }
]
```

---

# Screenshots

Screenshots of the working application are included in the `screenshots/` folder.

Recommended screenshots:

```text
01_dashboard.png
02_add_habit.png
03_habit_list.png
04_mark_complete.png
05_statistics.png
06_data_validation.png
```

---

# Project Objective

The objective of this project is to develop a simple and functional habit-tracking application while applying Python programming concepts such as:

- Functions
- Classes and objects
- Lists and dictionaries
- Conditional statements
- Loops
- File handling
- JSON processing
- Exception handling
- Input validation
- Modular programming
- GUI development
- Date and time processing

---

# Future Enhancements

Possible future improvements include:

- Calendar-based habit tracking
- Reminder notifications
- Graphical charts
- SQLite database integration
- User accounts
- Cloud synchronization
- CSV/PDF report generation
- Mobile application version

---

## Author

**Ritisha Daga**

**B.Tech CSE (Computing & Data Science)**  
**VIT Bhopal University**
