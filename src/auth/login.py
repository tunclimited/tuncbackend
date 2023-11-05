import json

import bcrypt
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource

from build.models.LoginResponse import LoginResponse
from src.tunclibs.send_to_node import InitMQ
import logging

logger = logging.getLogger("service-logger")


class Login(Resource):
    def post(self):
        logger.info(
            msg="Database call here service here rabbit 2 debug",
            extra={"tags": {"service": "my-service"}},
        )

        data = request.get_json()

        if 'username' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Missing data'}), 400

        new_user = {
            'username': data['username'],
            'email': data['email'],
            'password': data['password']
        }

        response = InitMQ.rpc_request(message=str(jsonify(new_user).json), QUEUE_NAME='login_queue')

        pw = response['password']
        hash = response['hash'][0]

        if response and bcrypt.checkpw(response['password'].encode(), response['hash'][0].encode()):
            access_token = create_access_token(identity=response['username'])
            refresh_token = create_refresh_token(identity=response['username'])


        logger.info(
            "User logged in successfully!",
            extra={"tags": {"service": "my-node"}},
        )

        resp_obj = LoginResponse(
            access_token = access_token,
            refresh_token = refresh_token
        )

        resp_dict = resp_obj.to_dict()

        return resp_dict
