
from flask import Flask,  request, jsonify

app = Flask(__name__)

users = {}

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
    user_add = request.get_json()
    username = user_add.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_add
    return jsonify({"message": "User added", "user": user_add}), 201

if __name__ == "__main__":
    app.run(debug=True)