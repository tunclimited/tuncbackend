from flask_restful import Resource

from src.tunclibs.send_to_node import InitMQ
import logging

logger = logging.getLogger("service-logger")

class Rabbit(Resource):
    def get(self):
        logger.info(
            msg="Something happened service here rabbit 1 debug",
            extra={"tags": {"service": "my-service"}},
        )

        response = InitMQ.rpc_request(message='dymanic message borkew', QUEUE_NAME='rpc_queue')

        return response
