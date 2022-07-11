import random
import pandas as pd


class Proxy:
    def __init__(self):
        pass

    def get(self):
        return None


class BonanzaProxy(Proxy):

    def __init__(self, filepath, random_state=None):
        self.random_state = random_state
        self.proxies = pd.read_csv(filepath)

    def get(self):
        proxy_data = self.proxies.sample(
            random_state=self.random_state).to_dict('records')

        proxy = "http://{}:{}@{}:{}".format(proxy_data[0]["login"],
                                            proxy_data[0]["password"],
                                            proxy_data[0]["ip"],
                                            proxy_data[0]["port_http"])
        return {"http": proxy, "https": proxy}
