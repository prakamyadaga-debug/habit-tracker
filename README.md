# Habit Tracker

A modular desktop Habit Tracker developed in Python using Tkinter and JSON.

## Features

- Add, edit and delete habits
- Mark habits complete for the current day
- Undo today's completion
- Persistent JSON data storage
- Current streak calculation
- Longest streak calculation
- Daily completion percentage
- Seven-day statistics
- Habit-wise performance statistics
- Input validation
- Modular project architecture
- User-friendly graphical interface

## Technology Stack

- Python 3.10+
- Tkinter
- JSON
- Object-oriented programming
- File handling
- Date/time processing

## Project Structure

```text
HabitTracker/
├── main.py
├── config.py
├── models.py
├── storage.py
├── habit_manager.py
├── analytics.py
├── validators.py
├── ui.py
├── utils.py
├── data/
│   └── habits.json
├── screenshots/
├── README.md
├── statement.md
└── requirements.txt
```

## How to Run

1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Open the VS Code terminal.
4. Run:

```bash
python main.py
```

On some systems use:

```bash
python3 main.py
```

## Data Storage

Habit information is stored locally in:

```text
data/habits.json
```

No internet connection or external database is required.

## Functional Requirements

1. The user can create a habit.
2. The user can edit a habit.
3. The user can delete a habit.
4. The user can mark a habit as completed.
5. The user can undo today's completion.
6. The system stores completion history.
7. The system calculates current streaks.
8. The system calculates longest streaks.
9. The system displays daily completion statistics.
10. The system displays seven-day statistics.

## Non-Functional Requirements

1. Usability: the interface should be easy to understand.
2. Reliability: data should persist between application sessions.
3. Maintainability: functionality is separated into modules.
4. Performance: normal operations should complete immediately for typical personal use.
5. Validation: invalid habit names and duplicate names are rejected.
6. Portability: the application uses standard Python libraries.

## Architecture

The project follows a simple layered architecture:

```text
User
  |
  v
Tkinter GUI (ui.py)
  |
  v
Habit Manager (habit_manager.py)
  |
  +--> Validators (validators.py)
  +--> Analytics (analytics.py)
  +--> Models (models.py)
  |
  v
Storage Layer (storage.py)
  |
  v
JSON File (data/habits.json)
```

## Academic Relevance

The project demonstrates:

- Variables and data types
- Lists and dictionaries
- Functions
- Classes and objects
- Conditional statements
- Loops
- File handling
- JSON data processing
- Exception handling
- Modular programming
- GUI programming
- Date/time operations
- Basic algorithmic thinking

## Testing Checklist

- [ ] Add a valid habit
- [ ] Try adding an empty habit
- [ ] Try adding a duplicate habit
- [ ] Edit a habit
- [ ] Delete a habit
- [ ] Mark a habit complete
- [ ] Undo completion
- [ ] Close and reopen the application
- [ ] Verify saved data
- [ ] Check current and longest streak
- [ ] Open statistics
