import importlib
import inspect
import os
import threading

import yaml

from src.tunclibs.queue_worker import QueueWorker


def import_message_handlers(script_dir):
    global imported_classes
    module_files = [f for f in os.listdir(os.path.join(script_dir, 'src/nodes')) if f.endswith('.py')]
    imported_classes = {}
    for module_file in module_files:
        module_name = os.path.splitext(module_file)[0]
        module = importlib.import_module(f"{'src.nodes'}.{module_name}")
        classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

        for class_obj in classes:
            class_name = class_obj.__name__
            imported_classes[class_name] = class_obj
            print(f'imported message handler: {class_name}')

    return imported_classes


def setup_broker_queues(imported_classes, script_dir):
    global workers
    with open(os.path.join(script_dir, 'src/common/queues.yaml'), 'r') as config_file:
        config = yaml.safe_load(config_file)
    workers = []
    for queue_config in config['queues']:
        queue_name = queue_config['name']
        for class_config in config['classes']:
            if class_config['queue'] == queue_name:
                callback_class_name = class_config['name']
                worker = QueueWorker(queue_name, imported_classes[callback_class_name])
                worker.connect()
                workers.append(worker)

    return workers


def start():
    threads = [threading.Thread(target=worker.start_consuming) for worker in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
