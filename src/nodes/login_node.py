import json
from sqlalchemy import text
from src.tunclibs.node_base import RabbitMQWorkerCallbackBase
from src.tunclibs.node_response import NodeResponse
import logging

from src.tunclibs.tunc_abstract import tunc

logger = logging.getLogger("node-logger")


class LoginClass(RabbitMQWorkerCallbackBase):
    @tunc
    def callback(self, ch, method, properties, body):
        decoded_string = body.decode('utf-8')
        string_with_double_quotes = decoded_string.replace("'", '"')

        json_obj = json.loads(string_with_double_quotes)

        username = json_obj['username']
        email = json_obj['email']
        password = json_obj['password']

        sql_query = text('select * from [TestProject].[dbo].[Users] where username = \'' + username + '\'')
        result = self.db_session.execute(sql_query)
        db_resp = result.fetchall()

        hash = db_resp[0][3]

        response = dict()
        response["username"] = username
        response["hash"] = hash,
        response["email"] = email,
        response["password"] = password

        resp_dict = response
        json_string = json.dumps(resp_dict, indent=4)

        NodeResponse.send_http_response(response=json_string, properties=properties, ch=ch, method=method)
