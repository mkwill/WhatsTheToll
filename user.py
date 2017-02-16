'''
Created on Jan 19, 2017

@author: micahwilliams
'''
from math import sqrt




class User(object):

    '''
    User object holds all data fields and methods relating to the User Data
    '''
    aS = ""
    lat = 0.0
    lon = 0.0
    url = ""
    city = ""
    country = ""
    isp = ""
    org = ""
    region = ""
    regionName = ""
    status = ""
    timeZone = ""
    zip = ""


    def __init__(self, aS, lat, lon: object, url, city, country, isp,
                 org,
                 region,
                 regionName,
                 status,
                 timeZone,
                 zip):
        self.aS = aS
        self.lat = lat
        self.lon = lon
        self.url = url
        self.city = city
        self.country = country
        self.isp = isp
        self.org = org
        self.region = region
        self.regionName = regionName
        self.status = status
        self.timeZone = timeZone
        self.zip = zip

    def compare_Points(self, TollStation):
        x1 = self.lat
        y1 = self.lon
        x2 = TollStation.StartLatitude
        y2 = TollStation.StartLongitude
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
