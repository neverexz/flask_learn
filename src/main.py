from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/tasks', methods=['POST'])
def solve_task():
    data = request.get_json()
    print(data) 
    if not 'task_description' in data or not 'task_schema' in data or not 'actions' in data or not 'max_count' in data:
        return jsonify({"commandList": ["ERROR"]}), 400 
    return jsonify({"commandList": data['task_description']}), 200

@app.route('/tasks', methods=['GET'])
def solve():
    return f'hello'

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, port=8080)
