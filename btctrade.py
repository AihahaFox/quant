import urllib, urllib2
import hashlib, hmac
import time
import json

class BtcTradeMarketApi:
    def __init__(self):
        self.base_url = 'https://api.btctrade.com/api/'
        self.params = {
        'coin': None
        # xcsa
        }

    def get_ticker(self, coin_name):
        ticker_url = self.base_url+'ticker'
        self.params['coin'] = coin_name
        params = urllib.urlencode(self.params)
        ticker = urllib.urlopen("%s?%s"%(ticker_url, params))
        ticker_data = json.loads(ticker.read())
        return ticker_data

    def get_depth(self, coin_name):
        depth_url = self.base_url+'depth'
        self.params['coin'] = coin_name
        params = urllib.urlencode(self.params)
        depth = urllib.urlopen("%s?%s"%(depth_url, params))
        depth_data = json.loads(depth.read())
        return depth_data

    def get_trades(self, coin_name):
        trades_url = self.base_url+'trades'
        self.params['coin'] = coin_name
        params = urllib.urlencode(self.params)
        trades = urllib.urlopen("%s?%s"%(trades_url, params))
        trades_data = json.loads(trades.read())
        return trades_data


class BtcTradeTradeApi:
    def __init__(self):
        self.base_url = 'https://api.btctrade.com/api/'
        self.public_key = '142cp-55d7v-x6y3m-de518-6vh8k-b1ets-mtvn6'
        self.secret_key = hashlib.md5('K,n)1-b{d9)-]Fw*G-N7v8r-!ysxh-a22~U-eJFBG').hexdigest()
        t = int(time.time())
        self.nonce = str(t)+str(time.time()-t)[2:5]

    def get_balance(self):
        balabce_url = self.base_url+'balance'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'signature': signature,
        'nonce': self.nonce,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(balabce_url, new_params)
        balance = urllib2.urlopen(req)

        balance_data = json.loads(balance.read())
        return balance_data

    def get_orders(self, coin_name, o_type, order='ASC'):
        orders_url = self.base_url+'orders'
        params = {
        'coin': coin_name,
        'key': self.public_key,
        'nonce': self.nonce,
        'type': o_type,
        'ob': order,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'coin': coin_name,
        'signature': signature,
        'key': self.public_key,
        'nonce': self.nonce,
        'type': o_type,
        'ob': order,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(orders_url, new_params)
        orders = urllib2.urlopen(req)

        orders_data = json.loads(orders.read())
        return orders_data

    def fetch_order(self, order_id):
        fetch_url = self.base_url+'fetch_order'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'id': order_id,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'id': order_id,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(fetch_url, new_params)
        fetch = urllib2.urlopen(req)

        fetch_data = json.loads(fetch.read())
        return fetch_data

    def cancel_order(self, id):
        cancel_url = self.base_url+'cancel_order'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'id': order_id,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'id': order_id,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(cancel_url, new_params)
        cancel = urllib2.urlopen(req)

        cancel_data = json.loads(cancel.read())
        return cancel_data

    def buy(self, coin_name, amount, price):
        buy_url = self.base_url+'buy'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(buy_url, new_params)
        buy = urllib2.urlopen(req)

        buy_data = json.loads(buy.read())
        return buy_data

    def sell(self, coin_name, amount, price):
        sell_url = self.base_url+'sell'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'version': 2
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'version': 2
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(sell_url, new_params)
        sell = urllib2.urlopen(req)

        sell_data = json.loads(sell.read())
        return sell_data


if __name__ == '__main__':
    market_api = BtcTradeMarketApi()
    trade_api = BtcTradeTradeApi()
    print market_api.get_ticker('doge')
    print trade_api.get_orders('doge', 'all')
    print trade_api.fetch_order('364224611')
    print trade_api.sell('doge', 500000, 0.05)
