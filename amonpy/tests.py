from amonpy.sender import Log, Exception
from amonpy.config import AmonConfig
from amonpy.config import config
import unittest
from nose.tools import eq_

# The web application should be on for this tests to pass
class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        self.exception = Exception()

    def test_http_log(self):
        config.protocol = 'http'
        config.address = 'http://127.0.0.1:2464'
        _ = self.log('test', ['debug','http'])
        eq_(_, 'http request ok')
    
    def test_zeromq_log(self):
        config.protocol = 'zeromq'
        config.address = 'localhost:5464'
        _ = self.log('test', ['debug','zeromq'])
        eq_(_, 'zeromq request ok')


    def test_log_dict(self):
        _ = self.log({"test": "something", "more_test": "another thing"}, 'debug')
        eq_(_, 'http request ok')

    def test_log_list(self):
        _ = self.log([1,2,3,4], 'debug')
        eq_(_, 'http request ok')

    def test_log_tags(self):
        _ = self.log({"test": "something", "test_another": "another thing"}, ['debug', 'benchmark'])
        eq_(_, 'http request ok')

    def test_http_exception(self):
        _ = self.exception({'message': 'test', 'exception_class': 'testhttpexception'})
        eq_(_, 'http request ok')
    
    
    def test_zeromq_exception(self):
        config.protocol = 'zeromq'
        config.address = 'localhost:5464'
        
        _ = self.exception({'message': 'test', 'exception_class': 'testzeromqexception'})
        eq_(_, 'zeromq request ok')



class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = AmonConfig()

    def test_application_key(self):
        self.config.application_key = 'test'
        eq_(self.config.application_key, 'test')

    def test_host(self):
        self.config.host = 'host'
        eq_(self.config.host, 'host')

    def test_port(self):
        self.config.port = 'port'
        eq_(self.config.port, 'port')

    def test_file(self):
        self.config.file = 'file'
        eq_(self.config.file, 'file')

    def test_offline(self):
        self.config.offline =  True
        eq_(self.config.offline, True)

