#!/usr/bin/env python3
"""Main Entrypoint for API"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Home route"""
    return jsonify({"message": "Welcome to the API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
