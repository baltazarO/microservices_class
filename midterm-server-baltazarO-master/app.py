from flask import Flask, jsonify, abort, request
import json

app = Flask(__name__)

@app.route('/api/intdata/<int:id>', methods=["GET"])
def hello(id):
    num=-id
    val=False
    if (id % 2) == 0:
        val=True
    else:
        val=False
    dict= {
        "even":"ds",
        "inverted":"sd"
    }
    dict["even"] = val
    dict["inverted"] = num
    return jsonify(dict)
