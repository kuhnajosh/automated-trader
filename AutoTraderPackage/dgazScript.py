'''
Created on Feb 26, 2018

@author: kuhnja, Tyrus Sonneborn

'''

# This is going to make us a lot of money because we're hackers
import gdax
import time
import threading
from threading import Thread

'''
Created March 2, 2018
Class for handling each individual coin, should be treated as a singleton due to 
threading capabilities. Order of coins is: BTC, ETH, LTC, BCH

@param granularity : pass in list granularity of the coins in seconds, default is 3600 seconds
@param MA_period : pass in list of the moving average period in relation to granularity. IE:
         if you want 10 candlesticks in your moving average pass in 10
        
@author: Josh Kuhn, Tyrus Sonneborn
'''
class CoinHandler():
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
            self.traders.append(TradeHandler(coin,self.ledger[coin]))
        
        self.start()
    # Create a method that runs all of the calculations and trades here by running through the TradeHandler objects
    # Each coinhandler will have it's own worker thread so that each can do the calculations separately, allowing for
    # higher resolution and more on time trades.
    def start(self):
        workers = []
        
        while True:
            time.sleep(1)
            for trader in self.traders:
                workers.append(target=trader.check_for_trade())
            
            for worker in workers:
                worker.start()
         
            for worker in workers:
                worker.join()
                
            worker = []
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
            
    
'''
Created March 3, 2018
Class for handling all of the trades for each individual coin, would be beneficial to try to implement
multi-threading so each can do calculations independent of each other. 

@param product_id: ticker symbol for the coin to be traded
@param subledger: the specific section of the ledger that corresponds to the ticker symbol

@author: Josh Kuhn, Tyrus Sonneborn 
'''    
class TradeHandler():
    
    def __init__(self, product_id, subledger):
        self.product_id = product_id
        self.client = subledger['client']
        self.granularity = subledger['granularity']
    
    
    # This is the method for checking for trades, should potentially keep a boolean attribute to signify if we are 
    # in a buy or sell position
    def check_for_trade(self):
        # TODO: REPLACE WITH ACTUAL CALCULATIONS
        time.sleep(0.2)
        print(self.product_id, self.client.get_product_ticker(self.product_id))



        
def main():
    handler = CoinHandler()
    while True:

        # should use threads for these         
        for product_id in handler.coins:           
            print(product_id, handler.get_price(product_id))
        
        print("")
if __name__ == "__main__": main()








