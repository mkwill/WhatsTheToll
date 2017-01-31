'''
Created on Jan 19, 2017

@author: micahwilliams
'''
from math import sqrt


class User(object):
    '''
    User object holds all data fields and methods relating to the User Data
    '''
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Getters
    def get_X(self):
        # Function returns X field
        return self.x

    def get_Y(self):
        # Function returns X field
        return self.y

    # Setters
    def set_X(self, x):
        # Function sets CurrentMessage field
        self.x = x

    def set_Y(self, y):
        # Function sets CurrentMessage field
        self.y = y

    def compare_Points(self, TollStation):
        x1 = self.get_X()
        y1 = self.get_Y()
        x2 = TollStation.get_StartLatitude()
        y2 = TollStation.get_StartLongitude()
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
