import urllib, urllib2
import hashlib, hmac
import time
import json

class JuBiMarketApi:
    def __init__(self):
        self.base_url = 'https://www.jubi.com/api/v1/'
        self.params = {
        'coin': None
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

    def get_orders(self, coin_name):
        orders_url = self.base_url+'orders'
        self.params['coin'] = coin_name
        params = urllib.urlencode(self.params)
        orders = urllib.urlopen("%s?%s"%(orders_url, params))
        orders_data = json.loads(orders.read())
        return orders_data

    def get_all_ticker(self, coin_name):
        allticker_url = self.base_url+'allticker'
        self.params['coin'] = coin_name
        params = urllib.urlencode(self.params)
        allticker = urllib.urlopen("%s?%s"%(allticker_url, params))
        allticker_data = json.loads(allticker.read())
        return allticker_data


class JuBiTradeApi:
    def __init__(self):
        self.base_url = 'https://www.jubi.com/api/v1/'
        self.public_key = 'rw9sw-x473p-trevv-r9gnq-bkksj-qxj98-r151s'
        self.secret_key = hashlib.md5('2&%h~-L2W$%-LXb4w-@u!Aa-Hb48x-n@xz@-eA[6R').hexdigest()
        t = int(time.time())
        self.nonce = str(t)+str(time.time()-t)[2:5]

    def get_balance(self):
        balabce_url = self.base_url+'balance'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'signature': signature,
        'nonce': self.nonce,
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(balabce_url, new_params)
        balance = urllib2.urlopen(req)

        balance_data = json.loads(balance.read())
        return balance_data

    def get_trade_list(self, date=0, o_type='open'):
        trade_list_url = self.base_url+'trade_list'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'type': o_type,
        'since': date
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'signature': signature,
        'key': self.public_key,
        'nonce': self.nonce,
        'type': o_type,
        'since': date
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(trade_list_url, new_params)
        trade_list = urllib2.urlopen(req)

        trade_list_data = json.loads(trade_list.read())
        return trade_list_data

    def get_trade_view(self, order_id, coin_name):
        trade_view_url = self.base_url+'trade_view'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'id': order_id,
        'coin': coin_name
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'id': order_id,
        'coin': coin_name
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(trade_view_url, new_params)
        trade_view = urllib2.urlopen(req)

        trade_view_data = json.loads(trade_view.read())
        return trade_view_data

    def trade_cancel(self, id, coin_name):
        trade_cancel_url = self.base_url+'trade_cancel'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'id': order_id,
        'coin': coin_name
        }
        params = urllib.urlencode(params)
        h = hmac.new(self.secret_key, params, hashlib.sha256)
        signature = h.hexdigest()
        new_params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'signature': signature,
        'id': order_id,
        'coin': coin_name
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(trade_cancel_url, new_params)
        cancel = urllib2.urlopen(req)

        cancel_data = json.loads(cancel.read())
        return cancel_data

    def buy(self, coin_name, amount, price):
        buy_url = self.base_url+'trade_add'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'type': 'buy'
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
        'type': 'buy'
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(buy_url, new_params)
        buy = urllib2.urlopen(req)

        buy_data = json.loads(buy.read())
        return buy_data

    def sell(self, coin_name, amount, price):
        sell_url = self.base_url+'trade_add'
        params = {
        'key': self.public_key,
        'nonce': self.nonce,
        'coin': coin_name,
        'amount': amount,
        'price': price,
        'type': 'sell'
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
        'type': 'sell'
        }
        new_params = urllib.urlencode(new_params)
        req = urllib2.Request(sell_url, new_params)
        sell = urllib2.urlopen(req)

        sell_data = json.loads(sell.read())
        return sell_data


market_api = JuBiMarketApi()
trade_api = JuBiTradeApi()
# print market_api.get_orders('btc')
print trade_api.get_balance()
print trade_api.get_trade_list(o_type='all')
# print trade_api.fetch_order('364224611')
# print trade_api.sell('doge', 500000, 0.05)
