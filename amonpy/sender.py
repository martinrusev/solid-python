from amonpy.config import config
from amonpy.protocols.http import _http
try:
    from amonpy.protocols.zeromq import _zeromq
except:
    pass # If zeromq is not installed, don't trigger errors

class Log(object):

    def __call__(self, message, tags='notset'):

        data = {}
        data['message'] = message
        data['tags'] = tags

        protocol = config.get('protocol', None)
        
        if protocol == 'http':
            return _http.post(data, type='log')
        elif protocol == 'zeromq':
            return _zeromq.post(data, type='log')

# Shortcuts
# import amonpy
# amonpy.log(message, tags='')
log = Log()

class Exception(object):

    def __call__(self, data):
        
        protocol = config.get('protocol', None)
        
        if protocol == 'http':
            return _http.post(data, type='exception')
        elif protocol == 'zeromq':
            return _zeromq.post(data, type='exception')
# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
