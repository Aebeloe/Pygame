'''
Created on 18/07/2015

@author: Mads
'''
import math
from test._test_multiprocessing import sqr

class vector(object):
    def __init__(self, list1, list2):
        self.diff =(list2[0]-list1[0], list2[1]-list1[1])
    
    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2+self.b**2)
    
    def unit(self):
        try:
            distance = self.distance()
            self.aunit = self.a / distance
            self.bunit = self.b / distance
            return self.aunit,self.bunit
        except ZeroDivisionError:
            distance = 5743
            self.aunit = self.a / distance
            self.bunit = self.b / distance
            return self.aunit,self.bunit