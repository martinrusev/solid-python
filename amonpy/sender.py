from amonpy.config import config
from amonpy.protocols.http import post_http

def log(message, tags='notset'):

    data = {'message': message, 'tags': tags}

    if config.protocol == 'http':
       return post_http(data, type='log')
    elif config.protocol == 'zeromq':
       from amonpy.protocols.zeromq import zeromq_handler
       
       return zeromq_handler.post(data, type='log')

def exception(data):
    
    if config.protocol == 'http':
        return post_http(data, type='exception')
    elif config.protocol == 'zeromq':
        return zeromq_handler.post(data, type='exception')

