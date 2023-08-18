#!/usr/bin/env python3

import requests
import json
import sys
from columnar import columnar
from lib.weather import Weather, Header

url: str = "https://wapi.unreliable.cloud/weather"
zipcode: int = sys.argv[1]
rawHeader: tuple = {
    'X-WAPI-Custom': 'raw'
}


class Dict2Object(object):
    """Convert dictionary to class object"""

    def __init__(self, d: dict) -> object:
        self.__dict__ = d


def getWeather(zipcode: int) -> None:
    """Get weather from weather API"""

    r = requests.get(f"{url}/{zipcode}", headers=rawHeader)
    rJson = json.loads(r.text)
    w = Dict2Object(rJson)

    headers = Header.city, Header.state, Header.temp, Header.humidity
    wC = Weather(w.city, w.state, w.temp, w.humidity)
    table = [[wC.city, wC.state, f"{wC.temp}F", f"{wC.humidity}%"]]

    weatherTBL = columnar(table, headers, no_borders=True,
                          preformatted_headers=True)

    return (weatherTBL)


if __name__ == '__main__':
    print(getWeather(zipcode))
