import logging_loki
import logging

from src.tunclibs.docker_networking_helper import is_running_in_docker


def setup_logger(logger_origin):
    if is_running_in_docker():
        url = "http://loki:3100/loki/api/v1/push"
    else:
        url = "http://localhost:3100/loki/api/v1/push"

    handler = logging_loki.LokiHandler(
        url=url,
        tags={"application": "my-app"},
        auth=("username", "password"),
        version="1",
    )

    logger = logging.getLogger(logger_origin)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def tunc_log(log_message, is_service=False):
    logger = logging.getLogger("service-logger" if is_service else "node-logger")
    logger.info(msg=log_message, extra={"tags": {"service": "my-service"} if is_service else "my-node"})
