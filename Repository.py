'''
Repository Class holds all database functions. Database is a SQLite
Created on Jan 7, 2017

@author: micahwilliams
'''

import sqlite3


class Repository(object):
    def __init__(self, recreate = False):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        if recreate:
            c.execute("drop table if exists TollStationData")
            c.execute("create table if not exists TollStationData \
                    (CurrentMessage text, \
                    CurrentToll integer, \
                    EndLatitude double, \
                    EndLocationName text, \
                    EndLongitude double, \
                    EndMilepost double, \
                    StartLatitude double, \
                    StartLocationName text, \
                    StartLongitude double, \
                    StartMilepost double, \
                    StateRoute text, \
                    TravelDirections text, \
                    TripName text)")
        self.commit()
        self.close()


    def create_table(self, c):
        c.execute("create table if not exists TollStationData \
        (CurrentMessage text, \
        CurrentToll integer, \
        EndLatitude double, \
        EndLocationName text, \
        EndLongitude double, \
        EndMilepost double, \
        StartLatitude double, \
        StartLocationName text, \
        StartLongitude double, \
        StartMilepost double, \
        StateRoute text, \
        TravelDirections text, \
        TripName text)")

    def update_data(self, TollStation):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        c.execute("update TollStationData set \
        CurrentMessage = ?, \
        CurrentToll = ?, \
        EndLatitude = ?, \
        EndLocationName = ?, \
        EndLongitude = ?, \
        EndMilepost = ?, \
        StartLatitude = ?, \
        StartLocationName = ?, \
        StartLongitude = ?, \
        StartMilepost = ?, \
        StateRoute = ?, \
        TravelDirections = ?, \
        TripName = ? where TripName = ?", (
            TollStation.get_CurrentMessage(),
            TollStation.get_CurrentToll(),
            TollStation.get_EndLatitude(),
            TollStation.get_EndLocationName(),
            TollStation.get_EndLongitude(),
            TollStation.get_EndMilepost(),
            TollStation.get_StartLatitude(),
            TollStation.get_StartLocationName(),
            TollStation.get_StartLongitude(),
            TollStation.get_StartMilepost(),
            TollStation.get_StateRoute(),
            TollStation.get_TravelDirection(),
            TollStation.get_TripName(),
            TollStation.get_TripName()
        )
                  )

        self.commit()
        self.close()

    def insert_data(self, TollStation):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        c.execute("insert into TollStationData \
        (CurrentMessage, \
        CurrentToll, \
        EndLatitude, \
        EndLocationName, \
        EndLongitude, \
        EndMilepost, \
        StartLatitude, \
        StartLocationName, \
        StartLongitude, \
        StartMilepost, \
        StateRoute, \
        TravelDirections, \
        TripName) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            TollStation.get_CurrentMessage(),
            TollStation.get_CurrentToll(),
            TollStation.get_EndLatitude(),
            TollStation.get_EndLocationName(),
            TollStation.get_EndLongitude(),
            TollStation.get_EndMilepost(),
            TollStation.get_StartLatitude(),
            TollStation.get_StartLocationName(),
            TollStation.get_StartLongitude(),
            TollStation.get_StartMilepost(),
            TollStation.get_StateRoute(),
            TollStation.get_TravelDirection(),
            TollStation.get_TripName()
        )
                  )

        self.commit()
        self.close()

    def commit_close(self):
        self.commit()
        self.close()

    def open_database(self):
        self = sqlite3.connect("TollData.sqlite")
        c = self.cursor()
        return c, self

    def read_data(self):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        r = c.execute("select * from TollStationData")
        r = r.fetchall()
        print(r)
        print("printed r")
        self.commit()
        self.close()

