from __future__ import absolute_import

import traceback
import inspect
import sys
import os

from django.core.urlresolvers import resolve
from django.conf import settings

from solidpy.handlers.base import SolidBaseHandler
from solidpy.utils.wsgi import get_headers, get_environ
from solidpy.utils.stack import get_lines_from_file

class SolidDjangoMiddleware(SolidBaseHandler):


	def process_exception(self, request, exc):	
		exception_dict = {}

		exception_dict.update(self.exception_info(exc, sys.exc_info()[2]))	
		exception_dict['request'] = self.request_info(request)

		self.send(exception_dict, settings.SOLID_CONFIG)


	def exception_class(self, exception):
		"""Return a name representing the class of an exception."""

		cls = type(exception)
		if cls.__module__ == 'exceptions':  # Built-in exception.
			return cls.__name__
		return "%s.%s" % (cls.__module__, cls.__name__)	

	def request_info(self, request):

		"""
		Return a dictionary of information for a given request.

		This will be run once for every request.
		"""

		# We have to re-resolve the request path here, because the information
		# is not stored on the request.
		view, args, kwargs = resolve(request.path)
		for i, arg in enumerate(args):
			kwargs[i] = arg

		parameters = {}
		parameters.update(kwargs)
		parameters.update(request.POST.items())

		environ = request.META

		return {
				"session": dict(request.session),
				'cookies': dict(request.COOKIES),
				'headers': dict(get_headers(environ)),
                'env': dict(get_environ(environ)),
				"remote_ip": request.META["REMOTE_ADDR"],
				"parameters": parameters,
				"action": view.__name__,
				"application": view.__module__,
				"method": request.method,
				"url": request.build_absolute_uri()
		}

	def exception_info(self, exception, tb):

		culprit_filepath, lineno, method, error = traceback.extract_tb(tb)[-1]

		print culprit_filepath
		context = get_lines_from_file(filepath=culprit_filepath, culprit_lineno=lineno)
		
		backtrace = []
		for tb_part in traceback.format_tb(tb):
			backtrace.extend(tb_part.rstrip().splitlines())

		return {
			"message": str(exception),
			"backtrace": backtrace,
			"context": context,
			"exception_class": self.exception_class(exception)
		}

