==================
amonpy
==================

Amonpy is the Python client for Amon

===============
 Installation
===============


1. Install the package with ``pip install amonpy`` or alternatively you can  
download the tarball and run ``python setup.py install``


=========
 Usage 
=========

::
    
    import amonpy
    
    amonpy.log(message)
    amonpy.log(message, ['list', 'of', 'tags'])


    data = {
        'exception_class': '',
        'url': '',
        'backtrace': '',
        'enviroment': '',
        'data': ''

    }
    
    amonpy.exception(data)

=========
 Options 
=========

By default amonpy takes the connection details from `/etc/amon.conf`, but you can change these values:

:: 

    import amonpy
    amonpy.config.host = 'http://yourhost'
    amonpy.config.port = your port


    # While testing or developing the app you can turn off amonpy
    amonpy.config.offline = True


================
 Logging to file 
================

::

    import amonpy
    amonpy.config.file = '/path/to/file'

    # amonpy will send a request to the Amon app and in addition to that will log 
    # your data to the specified file
    amonpy.log('data')

    
    # amonpy is still going to log your data to a file, if you set offline to true
    amonpy.config.file = '/path/to/file'
    amonpy.config.offline = True

================
 Django 
================

Using amonpy in Django is exactly the same as every other python library. You can customize the config options 
by adding them somewhere in `settings.py`

:: 

    # in settings.py
    import amonpy
    amon.config.host = 'http://host' 


To capture and log exceptions

:: 

   MIDDLEWARE_CLASSES = (        
    .....
    'amonpy.adapters.DjangoExceptionMiddleware'
    ) 

===============
 Requirements
===============


Python 2.6+

requests

