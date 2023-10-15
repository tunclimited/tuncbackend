from flask import Flask, jsonify
from flask_restful import Api
import json
from src.endpoints.rabbit import Rabbit
from src.endpoints.rabbit_two import RabbitTwo
from src.tunclibs import yaay_splash
from src.tunclibs.logging_setup import setup_logger
from src.tunclibs.swagger_setup import SwaggerSetup


yaay_splash.yaay_splash()
setup_logger('service-logger')

app = Flask(__name__)
api = Api(app)


def setup_endpoints():
    api.add_resource(Rabbit, '/rab')
    api.add_resource(RabbitTwo, '/rabtwo')


setup_endpoints()

app.register_blueprint(SwaggerSetup.init_swagger(), url_prefix='/swagger')


@app.route('/swagger.json')
def swagger():
    with open('src/common/swagger.json', 'r') as f:
        return jsonify(json.load(f))


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
