import json
import requests
from amonpy.config import config
from amonpy.exceptions import ConnectionException

class AmonRemoteHTTP(object):

    headers = {"Content-type": "application/json"}

    errors = {'connection': 'Could not establish connection to '}

    def jsonify(self, data):
        return json.dumps(data)

    def _post(self, url, data, headers=None):

        headers = headers if headers else self.headers
            
        # Append the application key if present
        if config['application_key']:
            url = "{0}/{1}".format(url, config['application_key'])
       
        # Don't post the data if offline is true
        if not config['offline']:
            r = requests.post(url, data, headers=headers, timeout=5)

            if r.status_code != 200:
                error = "{0}-{1}".format(self.errors['connection'], url)
                raise ConnectionException(error)
            else:
                return 'ok'

