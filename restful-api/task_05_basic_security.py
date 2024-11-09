from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth(scheme='Bearer')

"bassedata" 
users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}
tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}
"""
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
"""
@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run()