import exifread as ef
import googlemaps
from hw16.script16 import GpsDecoder


def _convert_to_degress(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


def getGPS(filepath):
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != 'N':
                lat_value = -lat_value
        else:
            return {}
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != 'E':
                lon_value = -lon_value
        else:
            return {}
        return lat_value, lon_value


file_path = 'image.jpg'
gps = getGPS(file_path)
lat, lng = gps[0], gps[1]

print(lat, lng)

gmaps = googlemaps.Client(key='AIzaSyC1ZA4M0cYJRQziX4jj0JgtRjc0LGWfMDk')
reverse_geocode_result = gmaps.reverse_geocode((lat, lng))

gpsDecod = GpsDecoder(reverse_geocode_result, lat, lng)
gpsDecod.printAddr()

