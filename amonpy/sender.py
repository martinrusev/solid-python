from amonpy.config import config
from amonpy.protocols.http import post_http
try:
    from amonpy.protocols.zeromq import post_zeromq
except:
    _zeromq = None # If pyzmq is not isntalled

def log(message, tags='notset'):

    data = {'message': message, 'tags': tags}

    if config.protocol == 'http':
       return post_http(data, type='log')
    elif config.protocol == 'zeromq':
       return post_zeromq(data, type='log')

def exception(data):
    
    if config.protocol == 'http':
        return post_http(data, type='exception')
    elif config.protocol == 'zeromq':
        return post_zeromq(data, type='exception')

