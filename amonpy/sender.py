from amonpy.config import config

if config['protocol'] == 'http':
    from amonpy.protocols.http import remote
elif config['protocol'] == 'zeromq':
    from amonpy.protocols.zeromq import remote

class Log(object):

    def __call__(self, message, tags='notset'):

        data = {}
        data['message'] = message
        data['tags'] = tags

        return remote._post(data, type='log')

# Shortcuts
# import amonpy
# amonpy.log(message, tags='')
log = Log()

class Exception(object):

    def __call__(self, data):
        return remote._post(data, type='exception')

# Shortcut
# import amonpy
# amonpy.exception()
exception = Exception()
