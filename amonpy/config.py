class AmonConfig(dict):

    defaults = {"protocol": "http", "address": "http://127.0.0.1:2464"}

    def __init__(self):
        dict.__init__(self, self.defaults)


    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))

config = AmonConfig()
