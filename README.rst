==================
amonpy
==================

Amonpy is the Python client for Amon

===============
 Installation
===============


1. Install the package with ``pip install amonpy`` or alternatively you can  
download the tarball and run ``python setup.py install``


===============
 Configuration 
===============


:: 

    import amonpy
    amonpy.config.address = 'http://amonhost:port'

    amonpy.config.protocol = 'http|zeromq'


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



================
 Django 
================

Using amonpy in Django is exactly the same as in every other python library. You can customize the config options 
by adding them somewhere in `settings.py`

:: 

    # in settings.py
    import amonpy
    amon.config.address = 'http://amonhost:port' 


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

