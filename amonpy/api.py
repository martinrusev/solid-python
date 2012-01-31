import json
import requests
from amonpy.exceptions import ConnectionException
from amonpy.config import config
import datetime

class AmonAPI(object):

    headers = {"Content-type": "application/json"}

    errors = {'connection': 'Could not establish connection to the Amon API.\
			Please ensure that the web application is running'}

    def jsonify(self, data):
        return json.dumps(data)

    def _post(self, url, data, headers=None):

        headers = headers if headers else self.headers
            
        # Log the data to file 
        if config.file:
            now = datetime.datetime.now()
            string = 'date: "{0}", data: {1}\n'.format(str(now)[:19], str(data))
            
            try:
                with open(config.file, 'a+') as f:
                    f.write(string)
            except:
                pass

        # Append the application key if present
        if config.application_key:
            url = "{0}?key={1}".format(url, config.application_key)
       
        # Don't post the data if offline is true
        if not config.offline:
            r = requests.post(url, data, headers=headers, timeout=5)

            if r.status_code != 200:
                raise ConnectionException(self.errors['connection'])
            else:
                return 'ok'


class Log(AmonAPI):

    def __call__(self, message, tags='notset'):
        url = config.connection_url() + '/api/log'

        log_data = {}
        log_data['message'] = message
        log_data['tags'] = tags

        data = self.jsonify(log_data)

        return self._post(url, data)

# Shortcuts
# import amonpy
# amonpy.log(message, level='')
log = Log()

class Exception(AmonAPI):

    def __call__(self, data):
        data = self.jsonify(data)
        url = config.connection_url() + '/api/exception'

        return self._post(url, data)

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
