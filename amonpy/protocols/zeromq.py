import zmq
from amonpy.config import config

class AmonRemoteZeroMQ(object):

    def post(self, data, type=None):
        context = zmq.Context()
        address = "tcp://{0}".format(config['address'])
        
        socket = context.socket(zmq.DEALER)
        socket.connect(address)
        socket.send_json({"type": type, "content": data})
        
        socket.close()
        context.term()

_zeromq = AmonRemoteZeroMQ()
