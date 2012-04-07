import json
import requests
from amonpy.config import config
from amonpy.exceptions import ConnectionException

def post_http(data, type=None):
    headers = {"Content-type": "application/json"}

    errors = {'connection': 'Could not establish connection to '}

    url = config.address
    if type == 'log':
        url = "{0}/api/log".format(url)
    elif type == 'exception':
        url = "{0}/api/exception".format(url)

    # Append the application key if present
    application_key = config.application_key
    if application_key:
        url = "{0}/{1}".format(url, config.application_key)
   
    # Don't post the data if offline is true
    if not config.offline:
        data = json.dumps(data)
        
        r = requests.post(url, data, headers=headers, timeout=5)

        if r.status_code != 200:
            error = "{0}-{1}".format(errors['connection'], url)
            raise ConnectionException(error)
        else:
            return 'http request ok'

