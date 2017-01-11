from src.airport import *
from src.plane import *

def test_for_empty_apron():
    airport = Airport()
    assert len(airport.apron) == 0

def test_for_landing_plane():
    airport = Airport()
    plane = Plane()
    airport.clear_landing(plane)
    assert len(airport.apron) == 1
