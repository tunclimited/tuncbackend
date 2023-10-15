from src.tunclibs.node_base import RabbitMQWorkerCallbackBase
from src.tunclibs.node_response import NodeResponse
import logging

logger = logging.getLogger("node-logger")


class YourCallbackClass1(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        # Implement your specific callback logic here
        response = f"Callback 1 received"

        logger.info(
            "Node here rabbit 1",
            extra={"tags": {"service": "my-node"}},
        )
        print(response)

        NodeResponse.send_http_response(response=response, properties=properties, ch=ch, method=method)