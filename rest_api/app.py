"""
Products REST API
--------------------
A simple Flask REST API with full CRUD operations over an
in-memory list of products. Data is not persisted — it resets
when the server restarts.

Endpoints:
    GET    /api/products       - list all products
    GET    /api/products/<id>  - get a single product
    POST   /api/products       - create a new product
    PUT    /api/products/<id>  - update an existing product
    DELETE /api/products/<id>  - delete a product
"""

from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


@app.route("/api/products", methods=["GET"])
def get_products():
    """Returns the full list of products."""
    return jsonify(products)


@app.route("/api/products/<int:id>", methods=["GET"])
def get_product(id):
    """Returns a single product by id, or a 404 error if not found.

    Args:
        id (int): the product's id.
    """
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@app.route("/api/products", methods=["POST"])
def create_product():
    """Creates a new product from the JSON body and appends it to the list.

    Requires "name" and "price"; "stock" defaults to 0 if not provided.
    """
    data = request.get_json()
    
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max(p["id"] for p in products) + 1
    
    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"],
        "stock": data.get("stock", 0)
    }
    
    products.append(new_product)
    
    return jsonify(new_product), 201


@app.route("/api/products/<int:id>", methods=["PUT"])
def update_product(id):
    """Updates an existing product's fields. Fields not provided in the
    request body keep their current value.

    Args:
        id (int): the product's id.
    """
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.get_json()
    
    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    product["stock"] = data.get("stock", product["stock"])
    
    return jsonify(product), 200


@app.route("/api/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    """Deletes a product by id.

    Args:
        id (int): the product's id.
    """
    product = next((p for p in products if p["id"] == id), None)
    if product:
        products.remove(product)
        return jsonify({"message": f"Product {id} deleted"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)