'''
Created on Mar 3, 2018
@author: Josh Kuhn, Tyrus Sonneborn
'''

class DataHandler():
    '''
    This class handles the data parsing and sending buy, sell, or hold signals to the trade handler/ simulator
    '''


    def __init__(self, product_id, subledger):
       self.granularity= subledger['granularity']
       self.client = subledger['client']
       self.MA_period = subledger['MA_period']
       self.product_id = product_id

#getClose = (open + high + low + close)/4
def getClose(self, open, high, low, close):
    return (open + high + low + close)/4

#getOpen = (prevOpen + prevClose)/2
def getOpen(self, prevOpen, prevClose):
    return (prevOpen + prevClose)/2

#getHigh =  max(high, open, close)
def getHigh(self, high, open, close):
    return  max(high, open, close)

#getLow = min(low, open, close)
def getLow(self, low, open, close):
    return  min(low, open, close)