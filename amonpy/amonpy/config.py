import json

try:
	config_file = file('/etc/amon.conf').read()
	config = json.loads(config_file)
except:
	config = {}

_web_app = config.get('web_app', {})

settings = {
	'host': _web_app.get('host', 'http://127.0.0.1'),
	'port': _web_app.get('port', 2464)
}
