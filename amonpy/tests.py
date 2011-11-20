from api import Log, Exception
import unittest
from nose.tools import eq_

# The web application should be on for this tests to pass
class TestWebApp(unittest.TestCase):

	def setUp(self):
		self.log = Log()
		self.exception = Exception()

	def test_log(self):
		_ = self.log('test', level='debug')
		eq_(_, 'ok')
	
	def test_log_dict(self):
		_ = self.log({"test": "something", "more_test": "another thing"}, level='debug')
		eq_(_, 'ok')
	
	def test_log_list(self):
		_ = self.log([1,2,3,4], level='debug')
		eq_(_, 'ok')

	def test_exception(self):
		_ = self.exception({'message': 'test', 'exception_class': 'testexception'})
		eq_(_, 'ok')


class TestApi(unittest.TestCase):

	def setUp(self):
		self.log = Log()
		self.exception = Exception()

	def test_application_key(self):
		self.log.application_key = 'test'
		eq_(self.log.application_key, 'test')

		self.exception.application_key = 'test_again'
		eq_(self.exception.application_key, 'test_again')

	def test_host(self):
		self.log.host = 'host'
		eq_(self.log.host, 'host')

	def test_port(self):
		self.log.port = 'port'
		eq_(self.log.port, 'port')

