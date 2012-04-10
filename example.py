import amonpy
import sys
import traceback

# Http 
amonpy.config.address = 'http://127.0.0.1:2464'
for i in range(0, 100):
	amonpy.log('test data', ['debug','messages','http'])


# ZeroMQ
amonpy.config.address = '127.0.0.1:5464'
amonpy.config.protocol = 'zeromq'
amonpy.log('test data zeromq', ['debug','messages', 'zeromq'])


try:
    1/0
except Exception, e:
    type, value, backtrace = sys.exc_info()
    
    data = {
        'exception_class': e.__class__.__name__,
        'backtrace': traceback.format_exception(type, value, backtrace) ,
        'enviroment': '',
        'data': {"message": "test"}
    }

    amonpy.exception(data)
