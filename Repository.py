'''
Repository Class holds all database functions. Database is a SQLite
Created on Jan 7, 2017

@author: micahwilliams
'''
import os
import psycopg2
import urllib
from flask import json

class Repository(object):
    def __init__(self, recreate=False):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        if recreate:
            c.execute("drop table if exists TollStationData")
            c.execute("drop table if exists UserData")
        c.execute("create table if not exists TollStationData \
                    (CurrentMessage text, \
                    CurrentToll integer, \
                    EndLatitude decimal, \
                    EndLocationName text, \
                    EndLongitude decimal, \
                    EndMilepost decimal, \
                    StartLatitude decimal, \
                    StartLocationName text, \
                    StartLongitude decimal, \
                    StartMilepost decimal, \
                    StateRoute text, \
                    TravelDirections text, \
                    TripName text)")
        c.execute("create table if not exists UserData \
                    (lat decimal, \
                    lon decimal, \
                    url text, \
                    city text, \
                    country text, \
                    isp text, \
                    org text, \
                    region text, \
                    regionName text, \
                    status text, \
                    timeZone text, \
                    zip text)")
        self.commit()
        self.close()

    def create_table(self, c):
        c.execute("create table if not exists TollStationData \
        (CurrentMessage text, \
        CurrentToll integer, \
        EndLatitude decimal, \
        EndLocationName text, \
        EndLongitude decimal, \
        EndMilepost decimal, \
        StartLatitude decimal, \
        StartLocationName text, \
        StartLongitude decimal, \
        StartMilepost decimal, \
        StateRoute text, \
        TravelDirections text, \
        TripName text)")

    def update_data(self, TollStation):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        c.execute("update TollStationData set \
        CurrentMessage = %s, \
        CurrentToll = %s, \
        EndLatitude = %s, \
        EndLocationName = %s, \
        EndLongitude = %s, \
        EndMilepost = %s, \
        StartLatitude = %s, \
        StartLocationName = %s, \
        StartLongitude = %s, \
        StartMilepost = %s, \
        StateRoute = %s, \
        TravelDirections = %s, \
        TripName = %s where TripName = %s", (
            TollStation.CurrentMessage,
            TollStation.CurrentToll,
            TollStation.EndLatitude,
            TollStation.EndLocationName,
            TollStation.EndLongitude,
            TollStation.EndMilepost,
            TollStation.StartLatitude,
            TollStation.StartLocationName,
            TollStation.StartLongitude,
            TollStation.StartMilepost,
            TollStation.StateRoute,
            TollStation.TravelDirection,
            TollStation.TripName,
            TollStation.TripName
        )
                  )

        self.commit()
        self.close()

    def get_distances(self, User):
        c, self = self.open_database()
        distance = c.execute("SELECT startlocationname, currentmessage, currenttoll "
                  "FROM tollstationdata "
                  "CROSS JOIN userdata "
                  "WHERE url = (%s) and num = "
                  "(SELECT num FROM userdata WHERE url = (%s) ORDER BY num DESC limit 1) "
                  "ORDER BY sqrt(pow(startlatitude-lat,2)+pow(startlongitude-lon,2)) limit 3", (User.url, User.url))
        data = c.fetchall()
        return json.dumps(data)


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
        TripName) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            TollStation.CurrentMessage,
            TollStation.CurrentToll,
            TollStation.EndLatitude,
            TollStation.EndLocationName,
            TollStation.EndLongitude,
            TollStation.EndMilepost,
            TollStation.StartLatitude,
            TollStation.StartLocationName,
            TollStation.StartLongitude,
            TollStation.StartMilepost,
            TollStation.StateRoute,
            TollStation.TravelDirection,
            TollStation.TripName
        )
                  )

        self.commit()
        self.close()

    def insert_user(self, User):
        # This function inserts user data into database
        c, self = self.open_database()
        c.execute("insert into UserData \
        (lat, \
        lon, \
        url, \
        city, \
        country, \
        isp, \
        org, \
        region, \
        regionName, \
        status, \
        timeZone, \
        zip) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            User.lat,
            User.lon,
            User.url,
            User.city,
            User.country,
            User.isp,
            User.org,
            User.region,
            User.regionName,
            User.status,
            User.timeZone,
            User.zip
        )
                  )

        self.commit()
        self.close()

    def create_user_table(self):
        c, self = self.open_database()
        c.execute("create table if not exists UserData \
        (as text, \
        lat decimal, \
        lon decimal, \
        url text, \
        city text, \
        country text, \
        isp text, \
        org text, \
        region text, \
        regionName text, \
        status text, \
        timeZone text, \
        zip text)")
        self.commit()
        self.close()

    def open_database(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ['DATABASE_URL'])
        self = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        c = self.cursor()
        return c, self

    def read_data(self):
        # This function creates the database table to hold data from WSDOT API
        c, self = self.open_database()
        r = c.execute("select * from TollStationData")
        r = r.fetchall()
        print(r)
        self.commit()
        self.close()
