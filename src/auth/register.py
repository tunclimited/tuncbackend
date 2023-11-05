from flask import request, jsonify, Blueprint
from flask_restful import Resource

from src.tunclibs.send_to_node import InitMQ
import logging

logger = logging.getLogger("service-logger")


class Register(Resource):
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

        response = InitMQ.rpc_request(message=str(jsonify(new_user).json), QUEUE_NAME='register_queue')

        return response
