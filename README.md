# Python Habit Tracker

## 1. Project Title

**Python Habit Tracker**

A simple desktop application developed in Python to help users create, manage, and track their daily habits.

---

## 2. Project Overview

The **Python Habit Tracker** is a graphical desktop application that allows users to maintain a list of personal habits and track their daily progress.

The application provides an easy-to-use interface where users can add new habits, mark habits as completed, view their current progress, and remove habits when they are no longer required.

Habit data is stored locally using a **JSON file**, allowing the information to remain available when the application is closed and opened again.

The project demonstrates the practical use of **Python programming, Tkinter GUI development, functions, lists, dictionaries, file handling, and JSON data storage**.

---

## 3. Features

### Habit Management

* Add new habits.
* View existing habits.
* Delete habits.
* Mark habits as completed.

### Progress Tracking

* Track daily habit completion.
* Display the completion status of each habit.
* Reset completion status for a new day.

### Data Storage

* Store habit information locally.
* Save data automatically in a JSON file.
* Load previously saved habits when the application starts.

### User Interface

* Simple graphical user interface.
* Buttons and input fields for user interaction.
* Clear display of habit status.
* Beginner-friendly design.

---

## 4. Technologies / Tools Used

| Technology / Tool  | Purpose                             |
| ------------------ | ----------------------------------- |
| **Python 3**       | Main programming language           |
| **Tkinter**        | Graphical User Interface            |
| **JSON**           | Local data storage                  |
| **File Handling**  | Reading and writing habit data      |
| **Git & GitHub**   | Version control and project hosting |
| **VS Code / IDLE** | Code development and execution      |

### Python Concepts Used

* Variables
* Lists
* Dictionaries
* Functions
* Conditional statements
* Loops
* User input
* File handling
* JSON
* Exception handling
* Tkinter widgets
* Event-driven programming

---

## 5. Project Structure

```text
Habit-Tracker/
│
├── habit_tracker.py
├── habits.json
└── README.md
```

> `habits.json` may be created automatically when the application is first executed.

---

## 6. Installation & Setup

### Step 1: Install Python

Install **Python 3.x** on your computer.

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/YourUsername/habit-tracker.git
```

Move into the project directory:

```bash
cd habit-tracker
```

### Step 3: Check Tkinter

Tkinter is normally included with Python.

No external Python libraries are required for the basic version of this project.

### Step 4: Run the Application

```bash
python habit_tracker.py
```

The Habit Tracker GUI should open.

---

## 7. How to Use

### Add a Habit

1. Enter the name of the habit.
2. Click the **Add Habit** button.
3. The habit will appear in the habit list.

### Complete a Habit

1. Select the required habit.
2. Click the **Complete / Mark Done** button.
3. The habit's completion status will be updated.

### Delete a Habit

1. Select the habit you want to remove.
2. Click the **Delete** button.
3. The habit will be removed from the list.

### Save Data

Habit information is stored in the local JSON file so that the data can be loaded again when the application is restarted.

---

## 8. Instructions for Testing

The following test cases can be used to verify that the application works correctly.

| Test Case | Action                                       | Expected Result                                 |
| --------- | -------------------------------------------- | ----------------------------------------------- |
| **TC01**  | Start the application                        | GUI opens successfully                          |
| **TC02**  | Add a new habit                              | Habit appears in the list                       |
| **TC03**  | Add multiple habits                          | All habits appear correctly                     |
| **TC04**  | Mark a habit as completed                    | Completion status changes                       |
| **TC05**  | Delete a habit                               | Selected habit is removed                       |
| **TC06**  | Close and reopen the application             | Previously saved habits are loaded              |
| **TC07**  | Try adding an empty habit                    | Application prevents invalid input              |
| **TC08**  | Select an invalid/non-existing item          | Application handles the action without crashing |
| **TC09**  | Restart the application after making changes | Updated data remains available                  |
| **TC10**  | Reset daily progress                         | Completion status is reset correctly            |

### Basic Testing Procedure

1. Launch the application.
2. Add at least three different habits.
3. Mark one or more habits as completed.
4. Check that the completion status is displayed correctly.
5. Delete one habit.
6. Close the application.
7. Open the application again.
8. Verify that the remaining habit data has been saved correctly.
9. Test invalid inputs such as an empty habit name.
10. Confirm that the application does not crash.
    
## 09. Expected Result

After successfully running the program, a graphical Habit Tracker window should appear.

The user should be able to:

* Add habits
* View habits
* Mark habits as completed
* Delete habits
* Save habit data
* Reload previously saved data

---

## 10. Learning Outcomes

Through this project, the following concepts are practiced:

* Python GUI development using Tkinter
* Functions and modular programming
* Lists and dictionaries
* File handling
* JSON data storage
* User input validation
* Event-driven programming
* Basic application design
* Testing and debugging
* GitHub project documentation

---

## 11. Author

**Ritisha Daga**

B.Tech CSE (Computing & Data Science)

---

## 12. License

This project is developed for **educational and academic purposes**.
