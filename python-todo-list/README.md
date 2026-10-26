# to-do-list
# Python To-Do List Application

A simple command-line To-Do List application built with Python. It allows users to create, view, and delete tasks while automatically recording the date and time when each task is created. Tasks are stored in a local text file, so they remain available after the program closes.

## Features

- **Add Tasks:** Create a task with a name and description.
- **Automatic Timestamps:** Record the date and time when a task is created.
- **View Tasks:** Display all saved tasks with their indexes, descriptions, and timestamps.
- **Delete Tasks:** Remove a task by specifying its index.
- **Persistent Storage:** Save tasks in a local `todo.txt` file.
- **Automatic File Creation:** Create the storage file if it does not exist.
- **Error Handling:** Handle missing files, invalid indexes, and invalid numeric input.

## Technologies Used

- **Python 3**
- `datetime` — to generate timestamps.
- File handling — to read and write tasks to a text file.
- Object-oriented programming (OOP) — to represent tasks using a class.
- Exception handling — to manage common errors.

## Project Structure

```text
python-todo-list/
├── main.py
├── todo.txt
└── README.md
```

- `main.py` — Contains the task class, file operations, menu, and main application logic.
- `todo.txt` — Stores tasks locally. It is created automatically when needed.
- `README.md` — Documents the project.

*Note: The filenames above are examples. Adjust them to match your actual project.*

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-todo-list.git
```

### 2. Navigate to the project directory

```bash
cd python-todo-list
```

### 3. Run the application

```bash
python3 main.py
```

No external Python packages are required.

## How to Use

After launching the application, you will see the following menu:

```text
=== ENTER A NUMBER ===
1. Add New task
2. View All tasks
3. Delete a task
4. Exit
```

### 1. Add a Task

Select `1`, enter the task name and description, and the application will automatically record the current date and time.

Example:

```text
the name of the task: Learn Python
the description: Practice classes and file handling
```

### 2. View All Tasks

Select `2` to display all saved tasks.

Example:

```text
0. task: Learn Python, desc: Practice classes and file handling, time: 2026-10-26 14:30:00
```

### 3. Delete a Task

Select
