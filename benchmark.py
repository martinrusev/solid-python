import time
import amonpy
import logging
import zmq
import urllib2
import json

runs = 5000
http_address = 'http://127.0.0.1:2464'
zeromq_address = '127.0.0.1:5464'

zeromq_bench = True
http_bench = False
standart_bench = True

print "Runs: {0}".format(runs)


class ZeroMQHandler():
    def __init__(self, socktype=zmq.DEALER):
        self.ctx = zmq.Context.instance()
        self.socket = zmq.Socket(self.ctx, socktype)
        
        address = "tcp://{0}".format(zeromq_address)
        self.socket.connect(address)

    def close(self):
        self.socket.close()

    def post(self, data):
        self.socket.send_json(data, zmq.NOBLOCK)

if zeromq_bench is True:
    amonpy.config.address = zeromq_address
    amonpy.config.protocol = 'zeromq'

    start = time.time()
    for i in range(0, runs):
        amonpy.log({"key": "value"})

    print "ZeroMQ - {0}".format(time.time()-start) 
    
    
    #z = ZeroMQHandler()
    #start = time.time()
    #for i in range(0, runs):
        #data = {'content': {'message': 'zeromq test {0}'.format(i), 'tags': ['debug']}, 'type':'log'}
        #z.post(data)

    #print "ZeroMQ Raw - {0}".format(time.time()-start) 


if http_bench is True:
    amonpy.config.address = http_address
    amonpy.config.protocol = 'http'

    start = time.time()
    for i in range(0, runs):
        amonpy.log({"key": "value"})

    print "HTTP - {0}".format(time.time()-start) 


    start = time.time()
    for i in range(0, runs):
        data = {'message': 'test me', 'tags':['debug','test']}
        json_string = json.dumps(data)

        req = urllib2.Request("{0}/api/log".format(http_address),
                          headers = {"Content-Type": "application/json"},
                          data = json_string)
        f = urllib2.urlopen(req)

    print "HTTP Raw - {0}".format(time.time()-start) 


if standart_bench is True:
    logger = logging.getLogger('amonpy_application')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('bench.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    start = time.time()
    for i in range(0, runs):
        _dict = {"key": "value"}
        logger.info(str(_dict))

    print "Standard logging - {0}".format(time.time()-start) 


    

