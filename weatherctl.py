#!/usr/bin/env python3

import requests
import json
import sys
from columnar import columnar
from dataclasses import dataclass

url: str = "https://wapi.unreliable.cloud/weather"
#zipcode: int = sys.argv[1]
zipcode: int = 53716
rawHeader: tuple = {
    'X-WAPI-Custom': 'raw'
}

class Dict2Object(object):
    """Convert dictionary to class object"""
    def __init__(self, d: dict) -> object:
        self.__dict__ = d

@dataclass
class Weather:
    """Define weather properties"""
    city: str
    state: str
    temp: float
    humidity: int

    def weatherData(city: str, state: str, temp: float, humidity: int) -> list:
        """Nested list for creating table data"""
        data: list = [
            [
                city,
                state,
                temp,
                humidity
            ],
        ]

        return(data)

    def weatherHeader() -> list:
        """Define table column header"""
        header: list = [
            'City',
            'State',
            'Temp',
            'Humidity'
        ]

        return(header)

def getWeather(zipcode: int) -> None:
    r = requests.get(f"{url}/{zipcode}", headers=rawHeader)
    rJson = json.loads(r.text)
    weatherOutput = Dict2Object(rJson)
    headers: list = Weather.weatherHeader()
    data: list = Weather.weatherData(weatherOutput.city, weatherOutput.state, f"{weatherOutput.temp}F", f"{weatherOutput.humidity}%")
    table: str = columnar(data, headers, no_borders=True, preformatted_headers=True)

    return(table)


if __name__ == '__main__':
    print(getWeather(zipcode))