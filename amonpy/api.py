import json
import requests
from amonpy.exceptions import ConnectionException
from amonpy.config import settings

class AmonAPI(object):

	def __init__(self):
		self._app_key = None
		self._host = None
		self._port = None
	
	def get_application_key(self):
		return self._app_key

	def set_application_key(self, app_key):
		self._app_key = app_key
	
	app_key = property(get_application_key, set_application_key)
	
	def get_host(self):
		return self._host

	def set_host(self, host_address):
		self._host = host_address
	
	host = property(get_host, set_host)

	def get_port(self):
		return self._port

	def set_port(self, port):
		self._port = port
	
	port = property(get_port, set_port)

	def connection_host(self):
		local_hosts = ['127.0.0.1', 'localhost']
		hostaddr =  self._host if self._host else settings['host']
		
		if hostaddr in local_hosts:
			hostaddr =  "http://{0}".format(hostaddr)

		return hostaddr

	def connection_port(self):
		return self._port if self._port else settings['port']

	def connection_url(self):
		return "{0}:{1}".format(self.connection_host(), self.connection_port())
	
	
	headers = {"Content-type": "application/json"}

	errors = {'connection': 'Could not establish connection to the Amon API.\
			Please ensure that the web application is running'}

	def jsonify(self, data):
		return json.dumps(data)

	def _post(self, url, data, headers=None):
		
		headers = headers if headers else self.headers

		r = requests.post(url, data, headers=headers)

		if r.status_code != 200:
			raise ConnectionException(self.errors['connection'])
		else:
			return 'ok'
		

class Log(AmonAPI):

	def __init__(self):
		super(Log, self).__init__()

	def __call__(self, message, level='notset'):
		url = self.connection_url() + '/api/log'

		log_data = {}
		log_data['message'] = message
		log_data['level'] = level

		data = self.jsonify(log_data)

		return self._post(url, data)

# Shortcuts
# import amonpy
# amonpy.log(message, level='')
log = Log()

class Exception(AmonAPI):
	
	def __init__(self):
		super(Exception, self).__init__()

	def __call__(self, data):
		data = self.jsonify(data)
		url = self.connection_url() + '/api/exception'

		return self._post(url, data)

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
