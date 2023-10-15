from src.tunclibs.db_service import DatabaseService


class RabbitMQWorkerCallbackBase:
    db_session = None

    def __init__(self):
        session = DatabaseService()
        self.db_session = session.get_session()

    def callback(self, ch, method, properties, body):
        raise NotImplementedError("Subclasses must implement the callback method.")