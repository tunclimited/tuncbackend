import pika

from src.tunclibs.docker_networking_helper import is_running_in_docker


class QueueWorker:
    def __init__(self, queue_name, callback_class):
        self.queue_name = queue_name
        self.callback_class = callback_class
        self.connection = None
        self.channel = None

    def connect(self, host='rabbitmq'):
        if not is_running_in_docker():
            host = "localhost"

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)

    def callback(self, ch, method, properties, body):
        callback_instance = self.callback_class()
        callback_instance.callback(ch, method, properties, body)

    def start_consuming(self):
        print(f'Worker for queue "{self.queue_name}" is waiting for RPC requests. To exit, press Ctrl+C')
        self.channel.start_consuming()


class RabbitMQWorkerCallbackBase:
    def callback(self, ch, method, properties, body):
        raise NotImplementedError("Subclasses must implement the callback method.")
