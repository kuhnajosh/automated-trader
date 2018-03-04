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
       
    