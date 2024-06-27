from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat


app = Flask(__name__)
CORS(app)
api = Api(app)
chat = GigaChat(credentials='MTE0MWQxY2EtNzI3MC00MjY0LTkxZDUtZmQ1YTJlZjEzZmE0OmZlODZkZmI5LTMyNTEtNDdkMC1hYTBjLTlhODRjNWYxMGZkYg==', model ='GigaChat-Pro', verify_ssl_certs=False)

messages = [
    SystemMessage(content="")
]

base = "\nв овтете укажи только команды которые указаны в Доступные команды без комментариев"

def finder(data):
    messages.append(HumanMessage(content= data + base))
    res = chat(messages)
    messages.append(res)
    return res.content

class TaskResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task_description', type=str, required=True, help='Description of the task')
        parser.add_argument('task_schema', type=str, required=True, help='Schema of the task')
        parser.add_argument('actions', type=list, required=True, help='List of possible actions')
        parser.add_argument('max_count', type=int, required=True, help='Maximum number of actions')

        args = parser.parse_args(strict=True)
        k = str(args['actions']).split("[")
        prompt = str(args['task_description']) + str(args['actions'])[0]
        res = finder(prompt)
        return make_response(jsonify({'commandList': res.split('\n')}), 200)

api.add_resource(TaskResource, '/tasks')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
