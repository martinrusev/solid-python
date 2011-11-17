from api import log, exception
import unittest
from nose.tools import eq_

class TestApi(unittest.TestCase):

	def test_application_key(self):
		log.application_key = 'test'
		eq_(log.application_key, 'test')

		exception.application_key = 'test_again'
		eq_(exception.application_key, 'test_again')


	# The web application should be on for this test to pass
	def test_log(self):
		_ = log('test', level='debug')
		eq_(_, 'ok')

	def test_exception(self):
		_ = exception({'message': 'test'})
		eq_(_, 'ok')
