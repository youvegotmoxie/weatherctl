from dataclasses import dataclass


@dataclass
class Weather:
    """Define weather properties"""

    city: str
    state: str
    temp: int | float | str
    humidity: int | float | str


@dataclass
class Header(Weather):
    """Define table header from Weather object"""
    Weather.city = 'City'
    Weather.state = 'State'
    Weather.temp = 'Temp'
    Weather.humidity = 'Humidity'

    def __str__(self):
        return (f"{self}")
