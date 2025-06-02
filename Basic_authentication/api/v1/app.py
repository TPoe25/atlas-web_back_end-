#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.errorhandler(401)
def unauthorized(error):
    """Handle unauthorized access"""
    return jsonify({"error": "unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "forbidden"}), 403
