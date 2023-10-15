import os


def is_running_in_docker():
    # Check for common Docker environment variables
    return (
        os.environ.get("DOCKER_CONTAINER") == "true" or
        os.environ.get("DOCKER") == "true" or
        os.path.exists("/.dockerenv") or
        os.path.exists("/.dockerinit")
    )
