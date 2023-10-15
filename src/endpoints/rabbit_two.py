from flask_restful import Resource

from src.tunclibs.send_to_node import InitMQ


class RabbitTwo(Resource):
    def get(self):
        response = InitMQ.rpc_request(message='dymanic message borkew number 2', QUEUE_NAME='rpc_queue_2')

        return response

