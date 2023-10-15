import logging_loki
import logging


def setup_logger(logger_origin):
    handler = logging_loki.LokiHandler(
        url="http://localhost:3100/loki/api/v1/push",
        tags={"application": "my-app"},
        auth=("username", "password"),
        version="1",
    )

    logger = logging.getLogger(logger_origin)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
