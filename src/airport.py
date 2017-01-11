from random import randint

class Airport(object):

    def __init__(self):
        self.apron = []
        self.current_weather = self.weather()

    def weather(self):
        return randint(1, 5)

    def clear_landing(self, plane):
        self.apron.append(plane)

    def allow_takeoff(self, plane):
        self.apron.pop()
