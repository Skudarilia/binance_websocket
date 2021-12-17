import json
import asyncio
import re
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory


class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Server connected: {0}".format(response.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            json_message = json.loads(payload)
            candle = json_message['k']
            symbol = json_message['s']
            is_candle_closed = candle['x']

            if symbol == 'BTCUSDT':
                if is_candle_closed:
                    btcusdt.append(candle['c'])
                    print(symbol, end=': ')
                    print('%.2f' %calculate_sma(btcusdt))
            elif symbol == 'ETHUSDT':
                if is_candle_closed:
                    ethusdt.append(candle['c'])
                    print(symbol, end=': ')
                    print('%.2f' %calculate_sma(ethusdt))
            elif symbol == 'BNBBTC':
                if is_candle_closed:
                    bnbbtc.append(candle['c'])
                    print(symbol, end=': ')
                    print('%.6f' % calculate_sma(bnbbtc))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


def calculate_sma(sma_list):
    length = len(sma_list)
    summ = 0
    for i in sma_list:
        summ += float(i)
    return summ / length


if __name__ == '__main__':

    btcusdt = []
    ethusdt = []
    bnbbtc = []

    pairs = ['btcusdt', 'ethusdt', 'bnbbtc']
    interval = '1m'

    socket1 = f"wss://stream.binance.com:9443/ws/{pairs[0]}@kline_{interval}"
    socket2 = f"wss://stream.binance.com:9443/ws/{pairs[1]}@kline_{interval}"
    socket3 = f"wss://stream.binance.com:9443/ws/{pairs[2]}@kline_{interval}"

    factory1 = WebSocketClientFactory(socket1)
    factory1.protocol = MyClientProtocol

    factory2 = WebSocketClientFactory(socket2)
    factory2.protocol = MyClientProtocol

    factory3 = WebSocketClientFactory(socket3)
    factory3.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory1, "stream.binance.com", 9443, ssl=True)
    loop.run_until_complete(coro)

    coro = loop.create_connection(factory2, "stream.binance.com", 9443, ssl=True)
    loop.run_until_complete(coro)

    coro = loop.create_connection(factory3, "stream.binance.com", 9443, ssl=True)
    loop.run_until_complete(coro)

    loop.run_forever()

    loop.close()
