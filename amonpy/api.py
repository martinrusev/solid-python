import json
import requests
from amonpy.exceptions import ConnectionException
from config import settings

class AmonAPI(object):
		
	def get_application_key(self):
		return self.app_key

	def set_application_key(self, app_key):
		self.app_key = app_key

	application_key = property(get_application_key, set_application_key)	

	url = "{0}:{1}".format(settings['host'], settings['port'])
	headers = {"Content-type": "application/json"}

	errors = {'connection': 'Could not establish connection to the Amon API.\
			Please ensure that the web application is running'}

class Log(AmonAPI):

	def __init__(self):
		super(Log, self).__init__()

	def __call__(self, message, level='notset'):
		url = self.url + '/api/log'

		log_data = {}
		log_data['message'] = message
		log_data['level'] = level

		data = json.dumps(log_data)

		r = requests.post(url, data, headers=self.headers)

		if r.status_code != 200:
			raise ConnectionException(self.errors['connection'])
		else:
			return 'ok'

# Shortcuts
# import amonpy
# amonpy.log(message, level='')
log = Log()

class Exception(AmonAPI):
	
	def __init__(self):
		super(Exception, self).__init__()

	def __call__(self, data):
		data = json.dumps(data)
		url = self.url + '/api/exception'

		r = requests.post(url, data, headers=self.headers)

		if r.status_code != 200:
			raise ConnectionException(self.errors['connection'])
		else:
			return 'ok'

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
