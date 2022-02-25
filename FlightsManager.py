#Kyle R Fogerty
from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()
from FlightInfo import FlightInfo

class FlightsManager:
    def grabFlights(self):
        self.flights = fr_api.get_flights()
        self.flightInfos = []
        for flight in self.flights:
            flightInfo = FlightInfo(flight)
            if flightInfo.removable == False:
                self.flightInfos.append(flightInfo)
        


    def __init__(self):
        self.flights = None
        self.flightInfos = []
        self.grabFlights()

a = FlightsManager()