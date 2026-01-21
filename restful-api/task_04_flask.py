#!/usr/bin/python3
"""
Task 04: Simple API using Flask
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

# Status endpoint
@app.route("/status", methods=["GET"])
def status():
    return "OK"

# Get all usernames
@app.route("/data", methods=["GET"])
def get_usernames():
    return jsonify(list(users.keys()))

# Get user by username
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
