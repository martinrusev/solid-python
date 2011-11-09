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
    
    # Accepted levels - 'warning', 'error', 'info', 'critical', 'debug'
    amonpy.log(message, level=level)



    data = {
        'exception_class': '',
        'url': '',
        'backtrace': '',
        'enviroment': '',
        'data': ''

    }
    
    amonpy.exception(data)


===============
 Requirements
===============


Python 2.5+

requests

