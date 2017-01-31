'''
WhatsTheToll App will return current toll lane data pricing for closest HOT Lane station
todo:
    html
    closest gps calculator

@author: micahwilliams
'''

from flask import Flask
from Repository import *
from TollStation import *


app = Flask(__name__)
from routes import *


def get_toll_data():
    url = 'http://wsdot.wa.gov/traffic/api/api/tolling?AccessCode={964c5fc8-3d37-4aff-b833-4a464c5f3d53}'
    req = requests.get(url)
    data = req.json()
    return data

if __name__ == '__main__':
    import os
    TollData = Repository()
    TollStations = {}
    WSDATA = get_toll_data()
    i = 0
    for entry in WSDATA:
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
        #TollData.insert_data(TollStations[i])      #only use on recreate
        TollData.update_data(TollStations[i])
        i += 1

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

