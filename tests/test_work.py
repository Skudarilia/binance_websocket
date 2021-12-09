import unittest
from src.work import *


class TestWork(unittest.TestCase):
    def test_calculate_right(self):
        self.assertAlmostEqual(calculate_sma(['1']), 1)
        self.assertAlmostEqual(calculate_sma(['1', '3', '5', '7']), 4)
        self.assertAlmostEqual(round(calculate_sma(['1.5', '6.4', '3.3']), 2), 3.73)

    def test_calculate_wrong(self):
        self.assertNotAlmostEqual(calculate_sma(['100', '0']), 0)
        self.assertNotAlmostEqual(calculate_sma(['0.112', '145.36', '0.00001']), 0)

    def test_calculate_exception(self):
        self.assertRaises(TypeError, calculate_sma(['1aaaa']))
        self.assertRaises(TypeError, calculate_sma(['12.o3']))

    def test_server(self):
        pairs = ['btcusdt', 'ethusdt', 'bnbbtc']
        interval = '1m'

        socket1 = f"wss://stream.binance.com:9443/ws/{pairs[0]}@kline_{interval}"
        socket2 = f"wss://stream.binance.com:9443/ws/{pairs[1]}@kline_{interval}"
        socket3 = f"wss://stream.binance.com:9443/ws/{pairs[2]}@kline_{interval}"
        self.assertNotEqual(socket1, '')
        self.assertNotEqual(socket2, '')
        self.assertNotEqual(socket3, '')

        factory1 = WebSocketClientFactory(socket1)
        factory1.protocol = MyClientProtocol

        factory2 = WebSocketClientFactory(socket2)
        factory2.protocol = MyClientProtocol

        factory3 = WebSocketClientFactory(socket3)
        factory3.protocol = MyClientProtocol

        self.assertNotEqual(factory1, '')
        self.assertNotEqual(factory2, '')
        self.assertNotEqual(factory3, '')

        self.assertNotEqual(factory1.protocol, '')
        self.assertNotEqual(factory2.protocol, '')
        self.assertNotEqual(factory3.protocol, '')
