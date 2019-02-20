import pkg_resources
import random


class Proxy:
    def __init__(self):
        pass

    def get(self):
        return None


class BonanzaProxy(Proxy):

    def __init__(self, username, password):
        path = 'resources/proxies.txt'
        filepath = pkg_resources.resource_filename(__name__, path)
        self.username = username
        self.password = password
        with open(filepath) as f:
            self.proxies = f.readlines()

    def get(self):
        proxies = {}
        secure_random = random.SystemRandom()
        proxy = secure_random.choice(self.proxies)
        proxy = "http://{}:{}@{}".format(self.username,
                                         self.password,
                                         proxy)
        proxies['http'] = proxy
        proxies['https'] = proxy
        return proxies
