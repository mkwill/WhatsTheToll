'''
WhatsTheToll App will return current toll lane data pricing for closest HOT Lane station
todo:
    -finish database and methods
    -create toll lane class
    create user class
    html
    -gps services
    -get toll data method
    closest gps calculator

@author: micahwilliams
'''

from flask import Flask
from Repository import *
from TollStation import *
import requests

app = Flask(__name__)
from routes import *


def get_toll_data():
    url = 'http://wsdot.wa.gov/traffic/api/api/tolling?AccessCode={964c5fc8-3d37-4aff-b833-4a464c5f3d53}'
    req = requests.get(url)
    data = req.json()
    #     i = 0
    #     for entry in data:
    #         print(data[i])
    return data

if __name__ == '__main__':
    import os

    TollData = Repository()
    TollStations = {}
    WSDATA = get_toll_data()
    i = 0
    for entry in WSDATA:
        # print("Start of api data")
        TollStations[i] = TollStation(WSDATA[i]["CurrentMessage"],
                                      WSDATA[i]["CurrentToll"],
                                      WSDATA[i]["EndLatitude"],
                                      WSDATA[i]["EndLocationName"],
                                      WSDATA[i]["EndLongitude"],
                                      WSDATA[i]["EndMilepost"],
                                      WSDATA[i]["StartLatitude"],
                                      WSDATA[i]["StartLocationName"],
                                      WSDATA[i]["StartLongitude"],
                                      WSDATA[i]["StartMilepost"],
                                      WSDATA[i]["StateRoute"],
                                      WSDATA[i]["TravelDirection"],
                                      WSDATA[i]["TripName"], )
        #TollData.insert_data(TollStations[i])
        TollData.update_data(TollStations[i])
        i += 1
    #TollData.read_data()


    #user =  get_user_data()
    #print(user)


    app.run()

