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

    # Getters
    def get_CurrentMessage(self):
        # Function returns CurrentMessage field
        return self.CurrentMessage

    def get_CurrentToll(self):
        # Function returns CurrentToll field
        return self.CurrentToll

    def get_EndLatitude(self):
        # Function returns EndLatitude field
        return self.EndLatitude

    def get_EndLocationName(self):
        # Function returns EndLocation field
        return self.EndLocationName

    def get_EndLongitude(self):
        # Function returns EndLongtitude field
        return self.EndLongitude

    def get_EndMilepost(self):
        # Function returns EndMildpost field
        return self.EndMilepost

    def get_StartLatitude(self):
        # Function returns StartLatitude field
        return self.StartLatitude

    def get_StartLocationName(self):
        # Function returns StartLatitude field
        return self.StartLocationName

    def get_StartLongitude(self):
        # Function returns StartLongitude field
        return self.StartLongitude

    def get_StartMilepost(self):
        # Function returns StartMilepost field
        return self.StartMilepost

    def get_StateRoute(self):
        # Function returns StateRoute field
        return self.StateRoute

    def get_TravelDirection(self):
        # Function returns TravelDirection field
        return self.TravelDirection

    def get_TripName(self):
        # Function returns TripName field
        return self.TripName

    # Setters
    def set_CurrentMessage(self, newCurrentMessage):
        # Function sets CurrentMessage field
        self.CurrentMessage = newCurrentMessage

    def set_CurrentToll(self, newCurrentToll):
        # Function sets CurrentToll field
        self.CurrentToll = newCurrentToll