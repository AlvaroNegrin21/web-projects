"""
In-memory product data for the REST API.

Note: this is just a Python list, not a real database — data
resets every time the server restarts.
"""

products = [
    {"id": 1, "name": "Keyboard", "price": 49.99, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 29.99, "stock": 25},
    {"id": 3, "name": "Monitor", "price": 299.99, "stock": 5},
]