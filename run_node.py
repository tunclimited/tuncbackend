import os
from src.tunclibs import yaay_splash
from src.tunclibs.logging_setup import setup_logger
from src.tunclibs.message_broker_setup import import_message_handlers, setup_broker_queues, start


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaay_splash.yaay_splash()
    imported_classes = import_message_handlers(script_dir)
    workers = setup_broker_queues(imported_classes, script_dir)
    setup_logger('node-logger')
    start()
