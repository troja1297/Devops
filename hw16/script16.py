class GpsDecoder:
    gpsData = []
    m_lat = 0
    m_long = 0

    def __init__(self, gps, lat, lng):
        self.gpsData = gps
        self.m_lat, self.m_long = lat, lng

    def printAddr(self):
        address = self.gpsData[1].get('formatted_address')
        print("Input data: {}'; {}'".format(round(self.m_lat, 2), round(self.m_long, 2)))
        print("Output Data:")
        print("Location: {}".format(address))
        print("Google Maps URL: https://www.google.com/maps/search/?api=1&query={},{}".format(self.m_lat, self.m_long))

