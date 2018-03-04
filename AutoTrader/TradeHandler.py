'''
Created on Mar 3, 2018

@author: sonnebtb
'''
'''
Created March 3, 2018
Class for handling all of the trades for each individual coin, would be beneficial to try to implement
multi-threading so each can do calculations independent of each other. 

@param product_id: ticker symbol for the coin to be traded
@param subledger: the specific section of the ledger that corresponds to the ticker symbol

@author: Josh Kuhn, Tyrus Sonneborn 
'''    

import time, gdax, threading
from AutoTrader import DataHandler


class TradeHandler():
    
    def __init__(self, product_id, subledger):
        self.product_id = product_id
        self.client = subledger['client']    
    
    # This is the method for checking for trades, should potentially keep a boolean attribute to signify if we are 
    # in a buy or sell position
    def check_for_trade(self):
        # TODO: REPLACE WITH ACTUAL CALCULATIONS
        time.sleep(0.2)
        print(self.product_id, self.client.get_product_ticker(self.product_id))
    
    def print_some_shit(self):
        print(self)