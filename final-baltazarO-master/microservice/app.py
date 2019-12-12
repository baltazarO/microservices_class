from flask import Flask, jsonify, abort, request

app = Flask(__name__)

votes_list = [
  {
    'post_id': 0,
    'vote_count': -1
  },
  {
    'post_id': 1,
    'vote_count': 5
  },
  {
    'post_id': 2,
    'vote_count': 42
  }
]

@app.route('/api/votes/<int:id>', methods=["GET"])
def catbreed(id):
    if id < 0 or id >= len(votes_list):
        abort(404)
    return jsonify(votes_list[id])

@app.route('/api/votes', methods=["GET"])
def catbreeds():
    return jsonify(votes_list)
