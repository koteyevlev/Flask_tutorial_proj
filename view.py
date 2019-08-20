from app import app
from flask import Flask, jsonify

from models import Post

@app.route('/')
def index():
    name = 'Ivan'
    return jsonify({"about": "hello world"})

