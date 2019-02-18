from flask_restplus import Resource, fields
from flask import request
from api.api import api
import api.errors.api_error as api_error
from api.errors.messages import RUNTIME_ERROR

ns = api.namespace('health', description='health endpoint')

config = api.model('health', {
    'salute': fields.String(readOnly=False, description='salute your master')
})

@ns.route('/')
@api.response(404, 'Not found.')
@api.response(200, 'Ok.')
class HealthResource(Resource):

    @api.expect(config)
    @api_error.error(RUNTIME_ERROR)
    def put(self):
        """
        Put a sentence and get a salute

        Use this method to get the salute

        * Send a JSON object with the sentence.

        ```
        {
          "salute": "Hi master!"
        }
        ```

        * Get the response:
        """
        data = request.json
        salute = data.get("salute", None)
        from modules.factories.health_factory import HealthFactory
        hf = HealthFactory().instance()
        r = hf.process(salute=salute)
        return {'response': r}, 200

    def get(self):
        """
        Get a generic response, just for health check
        """
        return 'OK', 200
