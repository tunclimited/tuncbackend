from flask_restful import Resource

from src.tunclibs.send_to_node import InitMQ
import logging

logger = logging.getLogger("service-logger")

class RabbitTwo(Resource):
    def get(self):
        logger.info(
            msg="Database call here service here rabbit 2 debug",
            extra={"tags": {"service": "my-service"}},
        )
        response = InitMQ.rpc_request(message='dymanic message borkew number 2', QUEUE_NAME='rpc_queue_2')

        return response

