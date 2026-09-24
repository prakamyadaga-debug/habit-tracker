# Python Habit Tracker — Project Statement

## 1. Problem Statement

Many people want to build and maintain positive daily habits but find it difficult to consistently track their progress. Using paper-based methods or remembering habits mentally can make it difficult to monitor completion and maintain consistency.

The **Python Habit Tracker** addresses this problem by providing a simple desktop application where users can create habits, mark them as completed, and maintain their progress digitally.

The application stores habit information locally so that users can access their saved data when they restart the application.

---

## 2. Scope of the Project

The scope of this project is to develop a lightweight desktop-based habit tracking application using Python.

The project covers:

* Creating and managing personal habits.
* Displaying a list of existing habits.
* Marking habits as completed.
* Deleting unwanted habits.
* Tracking daily completion status.
* Saving habit information locally.
* Loading previously saved habit information.
* Providing a simple graphical user interface.
* Validating basic user input.
* Handling common user errors without crashing the application.

### Future Scope

The application can be further extended with:

* Weekly and monthly progress statistics.
* Habit completion percentages.
* Streak tracking.
* Reminders and notifications.
* Habit categories.
* Data visualization using charts.
* Search and filtering.
* Exporting habit data.
* Cloud-based synchronization.
* User accounts and multiple profiles.

---

## 3. Target Users

The application is designed for users who want a simple way to organize and monitor their daily habits.

### Primary Target Users

* **Students** — for tracking study, exercise, reading, and other academic or personal habits.
* **Working Professionals** — for maintaining productivity and personal routines.
* **Individuals Building New Habits** — for monitoring consistency in daily activities.
* **Beginners in Personal Productivity** — for users who prefer a simple habit-tracking system.

The application is particularly suitable for users who want a **simple offline desktop solution without requiring an online account**.

---

## 4. High-Level Features

### 4.1 Habit Creation

Users can enter and add new habits to their personal habit list.

### 4.2 Habit Display

The application displays the user's existing habits in an organized graphical interface.

### 4.3 Habit Completion

Users can mark a habit as completed when they finish the activity.

### 4.4 Habit Deletion

Users can remove habits that they no longer want to track.

### 4.5 Daily Progress Tracking

The application maintains the completion status of habits for the current tracking period.

### 4.6 Local Data Storage

Habit information is stored locally using a **JSON file**, allowing data to persist between application sessions.

### 4.7 Data Loading

Previously saved habit information is automatically loaded when the application starts.

### 4.8 Input Validation

The application checks user input and prevents basic invalid entries, such as adding an empty habit.

### 4.9 Graphical User Interface

The application provides an interactive GUI using **Tkinter**, allowing users to manage their habits through buttons, input fields, and list displays.
