try:
    import json
except:
    import simplejson as json

try:
    config_file = file('/etc/amon.conf').read()
    config_dict = json.loads(config_file)
except:
    config_dict = {}

_web_app = config_dict.get('web_app', {})

settings = {
        'host': _web_app.get('host', 'http://127.0.0.1'),
        'port': _web_app.get('port', 2464)
        }

class AmonConfig(object):

    def __init__(self):
        self._app_key = None
        self._host = None
        self._port = None
        self._file = None
        self._offline = None

    def get_application_key(self):
        return self._app_key

    def set_application_key(self, app_key):
        self._app_key = app_key

    application_key = property(get_application_key, set_application_key)

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

    def get_file(self):
        return self._file

    def set_file(self, file):
        self._file = file

    file = property(get_file, set_file)

    def get_offline(self):
        return self._offline

    def set_offline(self, offline):
        self._offline = offline

    offline = property(get_offline, set_offline)


    def connection_host(self):
        local_hosts = ['127.0.0.1', 'localhost']
        hostaddr =  self._host if self._host else settings['host']

        if hostaddr in local_hosts:
            hostaddr =  "http://{0}".format(hostaddr)

        # Add http if its a numeric ip address
        if not hostaddr.startswith('http'):
            hostaddr =  "http://{0}".format(hostaddr)

        return hostaddr

    def connection_port(self):
        return self._port if self._port else settings['port']

    def connection_url(self):
        return "{0}:{1}".format(self.connection_host(), self.connection_port())



config = AmonConfig()
