# 🌐 Web Projects — Flask

A collection of web development projects built with Flask, exploring routes, templates, forms, external APIs, and REST API design.

## 📂 Projects

| Project | Description | Concepts practiced |
|---------|-------------|---------------------|
| `intro_flask` | Minimal app to learn Flask basics | Routes, Jinja2 templates, template inheritance, static files |
| `task_manager` | Web-based task manager with JSON persistence | Forms, POST/GET, JSON storage |
| `weather_app` | Checks the current weather for any city | External APIs, dynamic templates |
| `rest_api` | REST API for managing products | Full CRUD (GET, POST, PUT, DELETE), JSON responses |

## 🛠️ How to run

Each project has its own folder and entry point. For example:

```bash
cd task_manager
python app.py
```

Then open **http://127.0.0.1:5000** in your browser (or use Postman/Thunder Client for `rest_api`).

### Requirements

```bash
pip install -r requirements.txt
```

Main dependency: `Flask`. `weather_app` also requires `requests`.

## 📚 About this repository

Projects built progressively while learning Flask, starting from basic routing and templates, moving to form handling and external API consumption, and finishing with a fully functional REST API.