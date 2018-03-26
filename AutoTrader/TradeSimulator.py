

'''
Created March 3, 2018
Class for handling all of the trades for each individual coin, would be beneficial to try to implement
multi-threading so each can do calculations independent of each other. 

@param product_id: ticker symbol for the coin to be traded
@param subledger: the specific section of the ledger that corresponds to the ticker symbol

@author: Josh Kuhn, Tyrus Sonneborn 
'''    

import time
import gdax
import threading
import AutoTrader.DataHandler as DataHandler


class TradeSimulator():
    
    def __init__(self, product_id, subledger, capital=100000):
        self.product_id = product_id
        self.client = subledger['client']
        self.granularity = subledger['granularity']
        self.capital = capital
        self.data_handler = DataHandler(product_id=product_id,subledger=subledger)
        self.bought_in = False 
    # This is the method for checking for trades, should potentially keep a boolean attribute to signify if we are 
    # in a buy or sell position
    def check_for_trade(self):
        # TODO: REPLACE WITH ACTUAL CALCULATIONS
        pass
        
        