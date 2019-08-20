from app import app
from flask import Flask, jsonify

@app.route('/')
def index():
    name = 'Ivan'
    return jsonify({"about": "hello world"})

