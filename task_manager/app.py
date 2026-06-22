"""
Task Manager (Web)
--------------------
A Flask web app to add, view, complete, and delete tasks, with
persistence in a JSON file. Web version of the console-based
task_manager_v2 project.
"""

from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    """Loads the list of tasks from the JSON file.

    Returns:
        list: list of tasks, or an empty list if the file doesn't exist.
    """
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Saves the list of tasks to the JSON file.

    Args:
        tasks (list): list of tasks to save.
    """
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

        
@app.route("/add", methods=["POST"])
def add():
    """Adds a new task from the submitted form and saves it."""
    task_name = request.form["task"]
    tasks = load_tasks()
    tasks.append({"name": task_name, "status": "pending"})
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/complete/<int:index>")
def complete(index):
    """Marks the task at the given index as completed and saves it.

    Args:
        index (int): index of the task in the list.
    """
    tasks = load_tasks()
    tasks[index]["status"] = "completed"
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    """Deletes the task at the given index and saves the result.

    Args:
        index (int): index of the task in the list.
    """
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
    return redirect(url_for("index"))
    

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)