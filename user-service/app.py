from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# In-memory user database for simplicity
users = {
    1: {"id": 1, "name": "John Doe", "email": "john@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
        
    data = request.get_json()
    user_id = max(users.keys()) + 1 if users else 1
    user = {
        "id": user_id,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users[user_id] = user
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
