#!/usr/bin/env python3
"""Flask app for Basic Authentication API."""

import os
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv('AUTH_TYPE')

if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden_error(error):
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request_handler():
    if auth is None:
        return

    excluded = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    if not auth.require_auth(request.path, excluded):
        return

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

from api.v1.views.index import app_views
app.register_blueprint(app_views)

if __name__ == '__main__':
    host = os.getenv('API_HOST', '0.0.0.0')
    port = os.getenv('API_PORT', '5000')
    app.run(host=host, port=int(port))
