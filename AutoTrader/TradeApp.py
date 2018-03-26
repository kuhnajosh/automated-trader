'''
Created on Feb 26, 2018

@author: kuhnja, Tyrus Sonneborn

'''

# This is going to make us a lot of money because we're hackers
'''
Created March 2, 2018
Class for handling each individual coin, should be treated as a singleton due to 
threading capabilities. Order of coins is: BTC, ETH, LTC, BCH

@param granularity : pass in list granularity of the coins in seconds, default is 3600 seconds
@param MA_period : pass in list of the moving average period in relation to granularity. IE:
         if you want 10 candlesticks in your moving average pass in 10
        
@author: Josh Kuhn, Tyrus Sonneborn
'''

from threading import Thread
import threading
import time

import gdax

import AutoTrader.TradeHandler as th, AutoTrader.TradeSimulator as ts



class TradeApp():
    coins = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'BCH-USD']
    
    
    def __init__(self, granularity=[3600, 3600, 3600, 3600], MA_period=[10, 10, 10, 10]): 
        self.clients = []
        
        # Create multiple clients to increase resolution of the calls, assigning
        # a new client to each coinA
        for i in range(0, 4):
            self.clients.append(gdax.PublicClient())
        
        self.ledger = {}
        
        # Put everything into a ledger that can be called, will eventually create objects that 
        # will manipulate and store this data 
        
        for i in range(0, 4):
            self.ledger[self.coins[i]] = {'client':self.clients[i], 'granularity':granularity[i], 'MA_period':MA_period[i]}
            
        self.traders = []
        
        #create the traders
        for coin in self.coins:
            self.traders.append(ts.TradeSimulator(coin,self.ledger[coin]))
        print('something1')
        self.start()
    # Create a method that runs all of the calculations and trades here by running through the TradeHandler objects
    # Each coinhandler will have it's own worker thread so that each can do the calculations separately, allowing for
    # higher resolution and more on time trades.
    def start(self):
        print('something')
        print(self.ledger['BTC-USD']['client'].get_product_historic_rates('BTC-USD',granularity=3600))
#         while True:
#             time.sleep(1)
#             for trader in self.traders:
#                 trader.check_for_trade()

    # Method to grab the price of the requested coin, will keep calling a new snapshot of the ledger
    # until price is in the ledger to prevent an exception from being thrown
    def get_latest_ticker(self, product_id):
        return self.ledger[product_id]['client'].get_product_ticker(product_id)
    
       
    # recursive call to get the price, insuring that there won't be exceptions thrown due to too many 
    # requests, or if no pricing information was given from the request
    def get_price(self, product_id):
        ledger_partition = self.get_latest_ticker(product_id)
        
        if not ledger_partition.__contains__('price'): 
            return self.get_price(product_id)
            
        return ledger_partition['price']


        
def main():
    print('something')
    handler = TradeApp()
#     while True:
# 
#         # should use threads for these         
#         for product_id in handler.coins:           
#             print(product_id, handler.get_price(product_id))
#         
#         print("")
if __name__ == "__main__": main()








