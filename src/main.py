from crypt import methods
from flask import Flask, make_response, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(12)
CORS(app, supports_credentials=True)

# Opening JSON file
f = open("data.json")
# returns JSON object as 
# a dictionary
data = json.load(f)

# return response 404 Not Found
def not_found():
    return make_response("Not Found", 404)


@app.route('/users', methods=["GET"])
def get_users_length():
    try:
        return make_response(jsonify({"usersLength": len(data["data"])}), 200)
    except:
        return not_found()


@app.route('/user/<int:num>', methods=["GET"])
def generate_users(num):
    try:
        return make_response(jsonify({"user": data["data"][num]}), 200)
    except:
        return not_found()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)