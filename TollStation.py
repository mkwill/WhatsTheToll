'''
Created on Jan 12, 2017

@author: micahwilliams
'''


class TollStation(object):
    '''
    TollStation object holds all data fields and methods relating to the TollStation Data
    Obtained from WSDOT API
    '''
    CurrentMessage = ""
    CurrentToll = 0
    EndLatitude = 0.0
    EndLocationName = ""
    EndLongitude = 0, 0
    EndMilepost = 0.0
    StartLatitude = 0.0
    StartLocationName = ""
    StartLongitude = 0.0
    StartMilepost = 0.0
    StateRoute = ""
    TravelDirection = ""
    TripName = ""

# constructor
    def __init__(self, CurrentMessage, CurrentToll, EndLatitude, EndLocationName, EndLongitude, EndMilepost,
                 StartLatitude, StartLocationName, StartLongitude, StartMilepost, StateRoute, TravelDirection,
                 TripName):
        self.CurrentMessage = CurrentMessage
        self.CurrentToll = CurrentToll
        self.EndLatitude = EndLatitude
        self.EndLocationName = EndLocationName
        self.EndLongitude = EndLongitude
        self.EndMilepost = EndMilepost
        self.StartLatitude = StartLatitude
        self.StartLocationName = StartLocationName
        self.StartLongitude = StartLongitude
        self.StartMilepost = StartMilepost
        self.StateRoute = StateRoute
        self.TravelDirection = TravelDirection
        self.TripName = TripName
