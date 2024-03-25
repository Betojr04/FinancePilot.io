from flask import Blueprint, request, jsonify
from .models import User, db
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
    
    if not name or not email or not password:
        return jsonify({'error': 'Name, Email, and Password are requrired.'}), 400
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    new_user = User(name=name, email=email, hashed_password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    access_token = create_access_token(identity=email)
    
    return jsonify({'message': "User Registered Successfully", 'access_token': access_token}), 200