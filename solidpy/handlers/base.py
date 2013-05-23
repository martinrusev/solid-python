import json
import requests

from solidpy.exceptions import ConnectionException


class SolidBaseHandler(object):

	def send(self, data, config_dict):
		headers = {"Content-type": "application/json"}

		errors = {'connection': 'Could not establish connection to '}


		url = config_dict.get('url', 'http://127.0.0.1:6464')
		secret_key = config_dict.get('secret', None)

		post_url = "{0}/api/exception/{1}".format(url, secret_key)

		data = json.dumps(data)
				
		r = requests.post(post_url, data, headers=headers, timeout=5)

		if r.status_code != 200:
			error = "{0}-{1}".format(errors['connection'], url)
			
			raise ConnectionException(error)

