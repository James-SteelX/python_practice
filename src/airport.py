class Airport(object):

    def __init__(self):
        self.apron = []

    def clear_landing(self, plane):
        self.apron.append(plane)
