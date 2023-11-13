import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource

from build.models.LoginResponse import LoginResponse
from src.tunclibs.logging_setup import tunc_log
from src.tunclibs.send_to_node import InitMQ


class Login(Resource):
    def post(self):
        tunc_log('A new login request has been made', True)
        data = request.get_json()

        if 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Missing data'}), 400

        new_user = {
            'username': data['username'],
            'email': data['email'],
            'password': data['password']
        }

        response = InitMQ.rpc_request(message=str(jsonify(new_user).json), QUEUE_NAME='login_queue')

        if response and bcrypt.checkpw(response['password'].encode(), response['hash'][0].encode()):
            access_token = create_access_token(identity=response['username'])
            refresh_token = create_refresh_token(identity=response['username'])

        resp_obj = LoginResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )

        resp_dict = resp_obj.to_dict()

        return resp_dict
