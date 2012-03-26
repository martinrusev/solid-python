class AmonConfig(dict):

    defaults = {"protocol": "http", 
                "host": "http://127.0.0.1",
                "port": 2464}

    def __init__(self):
        dict.__init__(self, self.defaults)


    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))

    def format_connection_host(self):
        local_hosts = ['127.0.0.1', 'localhost']

        if self.host in local_hosts:
            self.host =  "http://{0}".format(self.host)

        # Add http if its a numeric ip address
        if not self.host.startswith('http'):
            self.host =  "http://{0}".format(self.host)


    def connection_url(self):
        self.format_connection_host()
        #return "{0}:{1}".format(self.connection_host(), self.connection_port())
        print self['host']


config = AmonConfig()
