from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

posts = {"egor": {'gender': 'male', 'age': 20},
         "alex": {'gender': 'female', 'age': 27}}

videos = {}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

class Hello(Resource):
    def get(self, name, test):
        return posts[name]
    
    def post(self):
        return {"data": "Posted"}
    
class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    

api.add_resource(Hello, "/helloworld/<string:name>/<int:test>")
api.add_resource(Video, "/video/<int:video_id>")


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"user: {name}, id:{id}"

if __name__ == "__main__":
    app.run(debug=True)