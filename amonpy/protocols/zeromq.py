import zmq
from amonpy.config import config

class AmonRemoteZeroMQ(object):

    def post(self, data, type=None):
        address = "tcp://{0}".format(config.address)
        data = {"type": type, "content" : data}
        if config.application_key:
            data['application_key'] = config.application_key
        
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        socket.connect(address)
        
        try:
            socket.send_json(data)
        except Exception, e:
            raise e
        
        return 'zeromq request ok'
        
        socket.close()
        context.term()


_zeromq = AmonRemoteZeroMQ()
