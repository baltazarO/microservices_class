from flask import Flask, jsonify, abort, request, Response
from datetime import datetime   # looked at documentation on docs.python.org
from mongoengine import connect, StringField, IntField, Document, DateTimeField
from bson import json_util
import json
import pymongo
from bson import ObjectId
import os
import dns

import time



app = Flask(__name__)

myHost=os.environ['DB_HOST']
sleep_time = os.getenv('SLEEP_TIME', default=0)

db = connect(
    host=myHost,
    port=27017
)

class activity_log(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

@app.route('/api/activities/<string:ind>', methods=["GET"])
def activity(ind):
    data = activity_log.objects.get(id=ind).to_json()
    pyr = json.loads(data)
    return jsonify(pyr)

@app.route('/api/activities', methods=["GET"])
def activities():
    data = activity_log.objects.all().order_by('-timestamp').limit(10).to_json()
    pyr = json.loads(data)
    return jsonify(pyr)

@app.route('/api/activities', methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)
    new_act=json.dumps(request.get_json())
    dict = json.loads(new_act)
    collection = activity_log._get_collection()
    post_id = collection.insert_one(dict).inserted_id
    time.sleep(int(sleep_time))
    dict['_id'] = str(post_id)
    dict['id'] = str(post_id)
    dict['location'] = "/api/activities/" + str(post_id)
    js = json.dumps(dict)
    resp = jsonify(js)
    resp.status_code = 201
    return resp
