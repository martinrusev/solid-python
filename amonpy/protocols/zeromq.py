import zmq
from amonpy.config import config

class ZeroMQHandler():
    def __init__(self, socktype=zmq.DEALER):
        self.ctx = zmq.Context.instance()
        self.socket = zmq.Socket(self.ctx, socktype)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.setsockopt(zmq.SWAP, 25000000) # 25MB disk swap
        
        address = "tcp://{0}".format(config.address)
        self.socket.connect(address)

    def close(self):
        self.socket.close()

    def post(self, data, type=None):
        data = {"type": type, "content" : data}
        if config.application_key:
            data['app_key'] = config.application_key
        
        self.socket.send_json(data, zmq.NOBLOCK)

zeromq_handler = ZeroMQHandler()

