import time
import amonpy
import logging
#import profile

#def log_benchmark():
    #for i in range(0, 1000):
        #amonpy.log('test')
#profile.run('log_benchmark()')

amonpy.config.address = '127.0.0.1:5464'
amonpy.config.protocol = 'zeromq'

start = time.time()
for i in range(0, 1000):
    amonpy.log('test')

print "ZeroMQ - {0}".format(time.time()-start) 

amonpy.config.address = 'http://127.0.0.1:2465'
amonpy.config.protocol = 'http'

start = time.time()
for i in range(0, 1000):
    amonpy.log('test')

print "HTTP - {0}".format(time.time()-start) 

logger = logging.getLogger('amonpy_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('bench.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

start = time.time()
for i in range(0, 1000):
    logger.info('test')

print "Standard logging - {0}".format(time.time()-start) 
