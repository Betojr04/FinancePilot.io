from flask import Blueprint, request, jsonify
import json
import hashlib
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__)

"""
ROUTE TO REGISTER A NEW USER IN THE DATABASE
"""
@auth.route('/register', methods=['POST'])
def regiser_new_user():
    data = request.get_json()
    
    name = data['name']
    email = data['email']
    password = data['password']
    
    