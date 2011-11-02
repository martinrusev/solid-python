import json
import requests
from amonpy.exceptions import ConnectionException

class AmonAPI(object):
	
	url = 'http://127.0.0.1:2464'
	headers = {"Content-type": "application/json"}
	
	errors = {'connection': 'Could not establish connection to the Amon API.\
					Please ensure that the web application is running'}

class Log(AmonAPI):
	
	def __init__(self, url=None):
		if url != None:
			self.url = url

	def __call__(self, message, level='notset'):
		url = self.url + '/api/log'
		
		log_data = {}
		log_data['message'] = message
		log_data['level'] = level

		data = json.dumps(log_data)
		
		r = requests.post(url, data, headers=self.headers)

		if r.status_code != 200:
			raise ConnectionException(self.errors['connection'])

# Shortcuts
# import amonpy
# amonpy.log(message, level='')
log = Log()

class Exception(AmonAPI):
	
	def __init__(self, url=None):
		if url != None:
			self.url = url

	def __call__(self, data):
		data = json.dumps(data)
		url = self.url + '/api/exception'

		r = requests.post(url, data, headers=self.headers)

		if r.status_code != 200:
			raise ConnectionException(self.errors['connection'])

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
