import sys
import traceback


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
