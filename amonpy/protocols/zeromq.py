import zmq
from amonpy.config import config

def post_zeromq(data, type=None):
    address = "tcp://{0}".format(config.address)
    data = {"type": type, "content" : data}
    if config.application_key:
        data['app_key'] = config.application_key
    
    context = zmq.Context.instance()
    socket = context.socket(zmq.DEALER)
    socket.connect(address)
    
    try:
        socket.send_json(data, zmq.NOBLOCK)
    except Exception, e:
        raise e
    
    context.destroy()
    
    return 'zeromq request ok' # for the test suite
    

