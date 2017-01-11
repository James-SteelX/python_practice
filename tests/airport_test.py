from src.airport import *
from src.plane import *
import mock
from mock import Mock


def test_for_empty_apron():
    airport = Airport()
    assert len(airport.apron) == 0

def test_for_random_weather_number():
    with mock.patch('src.airport.Airport.weather') as mock_weather:
        mock_weather.return_value = (3)
        airport = Airport()
        assert airport.current_weather == 3

def test_for_landing_plane():
    airport = Airport()
    plane = Plane()
    airport.clear_landing(plane)
    assert len(airport.apron) == 1

def test_for_plane_take_off():
    airport = Airport()
    plane = Plane()
    airport.clear_landing(plane)
    airport.allow_takeoff(plane)
    assert len(airport.apron) == 0
