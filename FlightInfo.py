#Kyle R Fogerty

import csv
from FlightRadar24.api import FlightRadar24API

#Filter out unwanted data
class FlightQueryFilter:
    def setKeywords(self):
        if self.type == "miltary":
            self.keywords = ["Force","Army","Navy","force","army",'Unit ','unit ']
        else:
            self.keywords = []

    def __init__(self, type="miltary"):
        self.type = type
        self.setKeywords()
        



#Holds Information About Flights
class FlightInfo:

    def getAirline(self):
        with open('Code_Addresses/airline_codes.csv', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in csv_reader:
                    if (row[0] == self.flight.airline_iata and row[0] != "N/A" ) or (row[1] == self.flight.airline_icao and row[1] != "N/A"):
                        self.airline_name = row[2] if row[2] != '' else "N/A"
                        self.callsign = row[3] if row[3] != '' else "N/A"
                        self.country_flag = row[4] if row[4] != '' else "N/A"
                        self.comments = row[5] if row[5] != '' else "N/A"
                        return
        (self.airline_name) = None
        (self.callsign) = None
        (self.country_flag) = None
        (self.comments) = None
        return
    
    def checkComments(self):
        if self.comments == None:
            return
        for keyword in range(0, len(self.query_type.keywords)):
            if self.query_type.keywords[keyword] in self.comments:
                self.removable = False
                return
    def checkAirline(self):
        if self.airline_name == None:
            self.removable = True
            return
        for keyword in range(0, len(self.query_type.keywords)):
            if self.query_type.keywords[keyword] in self.airline_name:
                self.removable = False
                return
        self.removable = True
        return
    
    def getAircraftName(self):
        with open('Code_Addresses/aircraft_codes.csv', newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in csv_reader:
                    if (row[0] == self.flight.aircraft_code and row[0] != "N/A" ) or (row[1] == self.flight.aircraft_code and row[1] != "N/A"):
                        self.aircraft_name = row[2] if row[2] != '' else "N/A"
                        return
        self.aircraft_name = "Raw: " + self.flight.aircraft_code
        return

     #Print Information
    def printFlightInfo(self):
        print("Altitude: " + str(self.flight.altitude) + "ft " + "Coordinates: " + str(self.flight.latitude) + "," + str(self.flight.longitude))
        grounded = "Yes" if self.flight.on_ground == 1 else "No"
        print("Grounded: " + grounded)

    def printFullName(self):
        print(self.full_name if self.full_name != None else "Currently Unavailable")

    def printAircraftName(self):
        print(self.aircraft_name if self.aircraft_name != None else "Currently Unavailable")

    def gatherAdditionalInfo(self):
       # if self.flight.callsign == "DUKE47":
       #     print(self.flight)
        self.getAirline()
        self.checkComments()
        if self.removable == None:
            self.checkAirline()
        if self.removable == False:
            self.full_name = self.airline_name if self.airline_name != "N/A" else ""
            self.full_name += (": " + self.comments) if self.comments != "N/A" else ""
        if self.removable == False:
            print(self.flight.callsign)
            self.getAircraftName()
            self.printFullName()
            self.printAircraftName()
            self.printFlightInfo()
            print("")

   

    def __init__(self, flight, query_type=FlightQueryFilter(type="miltary")):
        self.flight = flight
        self.query_type = query_type
        self.removable = None
        self.gatherAdditionalInfo()