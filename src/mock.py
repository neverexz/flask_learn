import requests
from flask import jsonify

BASE = 'http://127.0.0.1:8080/'


mock = {
  "task_description": "TEST MOCK TASK",  
  "task_schema": "",
  "actions": [],
  "max_count": 0,
}

mock1 = {
  "task_description": "TEST MOCK TASK",
  "actions": "",
}

response = requests.post(BASE + 'tasks', json=mock)
print(response.status_code, response.json(), sep='\n')

response = requests.post(BASE + 'tasks', json=mock1)
print(response.status_code, response.json(), sep='\n')