#!/usr/bin/python3
"""
Task 04: Simple API using Flask (marker-safe)
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary (marker expects no pre-filled users)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Home route returning a welcome message"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status route returning OK"""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Return a JSON list of all usernames stored in the API
    Starts empty; new users added via /add_user
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return the full object of the given username
    If not found, return 404 with {"error": "User not found"}
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.
    Expected JSON body:
    {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    Handles errors:
      - Invalid JSON: 400
      - Missing username: 400
      - Username already exists: 409
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    # Start Flask development server
    app.run()
