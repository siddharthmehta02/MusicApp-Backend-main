from flask import Flask, request, jsonify
from bson.json_util import dumps
from flask_pymongo import pymongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CONNECTION_STRING = "mongodb+srv://dbUser:password123#@hello-world.k4vvt.mongodb.net/db?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db')
song_collection = db['Songs']
user_collection = db['Users']

@app.route('/', methods=['GET', 'POST'])
def index():
    online_users = db.list_collection_names()
    # userId = request.json['userId']
    return jsonify(online_users)
    # return 'success'

@app.route('/getAllSongs', methods=['GET','POST'])
def getAllSongs():
    songs = list(song_collection.find())
    return dumps(songs, indent = 2)

# @app.route('/postSongs', methods=['GET','POST'])
# def postSongs():
#     songs = []
#     print(len(songs))
#     song_collection.insert_many(songs)
#     # print(insert.inserted_ids)
#     return "success"

if __name__ == '__main__':
    app.run(debug=True) 