class AmonConfig(dict):

    def __init__(self):
        self._app_key = None
        self._address = 'http://127.0.0.1:2464'
        self._protocol = 'http'
        self._file = None
        self._offline = None

    def get_application_key(self):
        return self._app_key

    def set_application_key(self, app_key):
        self._app_key = app_key

    application_key = property(get_application_key, set_application_key)

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    address = property(get_address, set_address)

    def get_protocol(self):
        return self._protocol

    def set_protocol(self, protocol):
        self._protocol = protocol

    protocol = property(get_protocol, set_protocol)

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
 
config = AmonConfig()
