from simulation.simulationLoader import SimulationLoader
from simulation.robotManager import RobotManager

class Simulator:

    def __init__(self, scene):
        self.scene = scene
        self.path = "FleetCore/asset/scenario/sample.json"
        self.simulationLoader = SimulationLoader(self.path)
        self.simulationLoader.exportScenario(10, self.scene.graph)
        self.simulationLoader.readScenario()
        self.robotManager = self.simulationLoader.robotManager
    