from flask import Flask
from flask import jsonify

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

if __name__ == "__main__":
    app.run()