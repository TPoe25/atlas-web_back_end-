#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, request, jsonify, abort, make_response
from auth import Auth


app = Flask(__name__)
auth = Auth()

@app.route('/sessions', methods=['POST'])
def login():
    """Handle user login and create session"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        # Missing email or password
        abort(400, "Email and password are required")

    if not auth.valid_login(email, password):
        # Wrong email or password
        abort(401)

    session_id = auth.create_session(email)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response
