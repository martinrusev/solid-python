from amonpy.config import config
from amonpy.protocols.http import _http
try:
    from amonpy.protocols.zeromq import _zeromq
except:
    _zeromq = None # If pyzmq is not isntalled

def log(message, tags='notset'):

    data = {}
    data['message'] = message
    data['tags'] = tags

    if config.protocol == 'http':
        return _http.post(data, type='log')
    elif config.protocol == 'zeromq':
        return _zeromq.post(data, type='log')

def exception(data):
    
    if config.protocol == 'http':
        return _http.post(data, type='exception')
    elif config.protocol == 'zeromq':
        return _zeromq.post(data, type='exception')

