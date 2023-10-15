from flask import jsonify
import json
from flask_swagger_ui import get_swaggerui_blueprint


class SwaggerSetup:
    @staticmethod
    def init_swagger():
        SWAGGER_URL = '/swagger'
        API_URL = 'http://localhost:5000/swagger.json'
        return get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "Sample API"
            }
        )
