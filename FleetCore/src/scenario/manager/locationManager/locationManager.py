from scenario.manager.locationManager.pickManager import PickManager

class LocationManager:

    def __init__(self, graph):
        self.graph = graph
        self.pickManager = PickManager(self.graph)
    
        