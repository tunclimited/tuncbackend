from src.tunclibs.node_base import RabbitMQWorkerCallbackBase
from src.tunclibs.node_response import NodeResponse


class YourCallbackClass1(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        # Implement your specific callback logic here
        response = f"Callback 1 received"

        NodeResponse.send_http_response(response=response, properties=properties, ch=ch, method=method)