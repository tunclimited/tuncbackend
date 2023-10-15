import json

import pika

from src.tunclibs.docker_networking_helper import is_running_in_docker


class InitMQ:
    @staticmethod
    def rpc_request(message, QUEUE_NAME):
        if is_running_in_docker():
            url = "rabbitmq"
        else:
            url = "localhost"

        connection = pika.BlockingConnection(pika.ConnectionParameters(url))
        channel = connection.channel()

        # Declare a queue for sending requests
        channel.queue_declare(queue=QUEUE_NAME)

        # Declare a queue for receiving responses
        result = channel.queue_declare(queue='', exclusive=True)
        callback_queue = result.method.queue

        # Publish the request message to the RPC queue
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            properties=pika.BasicProperties(
                reply_to=callback_queue,
            ),
            body=message
        )

        response = None

        def on_response(ch, method, properties, body):
            nonlocal response
            response = body

        # Set up a consumer to listen for responses
        channel.basic_consume(
            queue=callback_queue,
            on_message_callback=on_response,
            auto_ack=True
        )

        while response is None:
            connection.process_data_events()

        connection.close()

        message_str = response.decode('utf-8')

        try:
            message_data = json.loads(message_str)
        except json.JSONDecodeError:
            message_data = message_str

        return message_data
