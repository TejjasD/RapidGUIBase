from scene.scene import Scene
from plot.window import Window
from simulation.simulator import Simulator
from scenario.manager.scenarioManager import ScenarioManager
from fleet.controller import Controller
from plot.plotMapper import PlotMapper

class FleetManager:

    def __init__(self):
        self.plotMapper = PlotMapper(1800, 900, 20)
        self.scene = Scene(self.plotMapper)
        self.simulator = Simulator(self.scene)
        self.scenarioManager = ScenarioManager(self.scene, self.simulator.robotManager)
        self.simulator = None
        self.plot = Window(self)
        self.controller = Controller(self.scenarioManager, self.scene)

    def exec(self):
        self.plot.exec()
    
    def step(self):
        self.scenarioManager.step()
        self.controller.step()