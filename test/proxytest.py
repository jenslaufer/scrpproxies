from unittest import TestCase
from scrpproxies.proxy import BonanzaProxy
import pandas as pd


class BonanazaProxyTest(TestCase):
    def setUp(self):
        self.proxy = BonanzaProxy("test/proxylist.csv")

    def test_get(self):
        proxy = self.proxy.get()
        self.assertIsNotNone(proxy["http"])
        self.assertIsNotNone(proxy["https"])
