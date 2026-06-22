"""
Intro to Flask
---------------
A minimal Flask app to learn the basics: routes, templates with
Jinja2, template inheritance, and serving static files (CSS).
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about_me")
def about_me():
    info = {
        "name": "Zhed",
        "description": "Python developer in training",
        "abilities": ["Python", "OpenCV", "MediaPipe", "Flask"]
    }
    return render_template("about_me.html", info=info)


@app.route("/")
def home():
    name = "Zhed"
    projects = ["Grade calculator", "Shopping cart", "Task manager", "Simple bank"]
    return render_template("index.html", name=name, projects=projects)


if __name__ == "__main__":
    app.run(debug=True)