import requests
from flask import request
from app import app
from user import User
from Repository import *
from TollStation import *
from math import sqrt


@app.route("/", methods=['Get', 'Post'])
def user_handler():
    TollData = Repository()
    TollStations = construct_TollsStations(TollData)
    data = get_data()
    user = User(data['as'], data['lat'], data['lon'], data['query'], data['city'], data['country'], data['isp'],
                data['org'], data['region'], data['regionName'], data['status'], data['timezone'], data['zip'])
    TollData.insert_user(user)
    return user.city


@app.route("/test", methods=['Get', 'Post'])
def test_handler():
    TollData = Repository()
    TollStations = construct_TollsStations(TollData)
    data = get_data()
    user = User(data['as'], data['lat'], data['lon'], data['query'], data['city'], data['country'], data['isp'],
                data['org'], data['region'], data['regionName'], data['status'], data['timezone'], data['zip'])
    TollData.insert_user(user)
    data = TollData.get_distances(user)
    return data






def get_data():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    url = 'http://ip-api.com/json/'
    url += ip
    req = requests.get(url)
    data = req.json()
    return data


def get_toll_data() -> object:
    url = 'http://wsdot.wa.gov/traffic/api/api/tolling?AccessCode={964c5fc8-3d37-4aff-b833-4a464c5f3d53}'
    req = requests.get(url)
    data = req.json()
    return data


def construct_TollsStations(TollData, TollStations={}, recreate=False):
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
        if recreate:
            TollData.insert_data(TollStations[i])
        else:
            TollData.update_data(TollStations[i])
        i += 1
    return TollStations


def compare_Points(user, TollStation):
    x1 = user.lat
    y1 = user.lon
    x2 = TollStation.StartLatitude
    y2 = TollStation.StartLongitude
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
