from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(5)
    return "Hello world!"

@app.route('/<name>')
def hello(name):
    time.sleep(5)
    return name
