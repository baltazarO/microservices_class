from mongoengine import connect, StringField, IntField, Document, DateTimeField
from datetime import datetime   # looked at documentation on docs.python.org
from flask import Flask, jsonify, abort, request
import os
import dns


db = connect(
    host=os.environ['DB_HOST'],
    port=27017
)

class activity_log(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

activity_log.objects.delete()
