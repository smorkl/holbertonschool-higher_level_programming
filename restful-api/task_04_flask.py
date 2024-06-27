from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """
    Retrieves and returns a list of all usernames in JSON format.
    """
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def get_status():
    """
    return ok
    """
    return ("OK")

@app.route("/users/<username>")
def get_user(username):
    """Retrieves and returns the full user object based on the username."""
    
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add a new user to the userdata based on the POST request data.
    """
    if request.method == "POST":
        try:
            user_data = request.get_json()
        except (KeyError, TypeError):
            return jsonify({"error": "Invalid JSON data provided"}), 400

        username = user_data.get("username")
        name = user_data.get("name")
        age = user_data.get("age")
        city = user_data.get("city")
    
        if not all([username, name]):
            return jsonify({"error": "Missing required fields (username and name)"}), 400

        users[username] = {"name": name, "age": age, "city": city}

        return jsonify({"message": "User added successfully", "user": users[username]})

    return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    app.run()