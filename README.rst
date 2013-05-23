==================
Solidpy
==================

Solidpy is the python Client for Solid

===============
 Installation
===============


1. Install the package with ``pip install solidpy`` or alternatively you can  
download the tarball and run ``python setup.py solidpy``


================
 Django 
================
To capture and log exceptions in settings.py add the following: 


:: 
	
	SOLID_CONFIG = {
		'url': 'http://solid_instance:port',
		'secret': 'secret_key'
	}


:: 

   MIDDLEWARE_CLASSES = (        
	.....
	'solidpy.handlers.django.DjangoExceptionMiddleware'
	) 

===============
 Requirements
===============


Python 2.6+

requests

