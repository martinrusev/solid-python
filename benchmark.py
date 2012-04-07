import time
import amonpy
import profile

amonpy.config.address = '127.0.0.1:5464'
amonpy.config.protocol = 'zeromq'

def log_benchmark():
    for i in range(0, 1000):
        amonpy.log('test')
profile.run('log_benchmark()')


#start = time.time()
#for i in range(0, 10000):
    #amonpy.log('test')

#print time.time()-start

