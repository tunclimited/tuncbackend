import json
import bcrypt
from sqlalchemy import text
from src.tunclibs.node_base import RabbitMQWorkerCallbackBase
from src.tunclibs.node_response import NodeResponse


class RegisterClass(RabbitMQWorkerCallbackBase):
    def callback(self, ch, method, properties, body):
        decoded_string = body.decode('utf-8')
        string_with_double_quotes = decoded_string.replace("'", '"')

        json_obj = json.loads(string_with_double_quotes)

        username = json_obj['username']
        email = json_obj['email']
        password = json_obj['password']

        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(bytes(password, 'utf-8'), salt)

        sql_query = text('insert into [TestProject].[dbo].[Users] values (\'' + username + '\', \'' + email +
                         '\', \'' + password_hash.decode() + '\', \'' + salt.decode() + '\')')

        self.db_session.execute(sql_query)
        self.db_session.commit()

        json_string = json.dumps({}, indent=4)

        NodeResponse.send_http_response(response=json_string, properties=properties, ch=ch, method=method)
