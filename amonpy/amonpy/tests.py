from api import log, exception
import unittest
from nose.tools import eq_

class TestApi(unittest.TestCase):

	def test_application_key(self):
		log.application_key = 'test'
		eq_(log.application_key, 'test')

		exception.application_key = 'test_again'
		eq_(exception.application_key, 'test_again')

