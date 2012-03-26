from amonpy.config import config

class Log(object):

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

class Exception(object):

    def __call__(self, data):
        data = self.jsonify(data)
        url = config.connection_url() + '/api/exception'

        return self._post(url, data)

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
