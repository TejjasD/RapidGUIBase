from scenario.manager.agentManager import AgentManager
from scenario.manager.locationManager.locationManager import LocationManager
from task.taskManager import TaskManager
from plot.plotMapper import PlotMapper

class ScenarioManager:

    def __init__(self, scene, robotManager):
        self.robotManager = robotManager
        self.scene = scene
        self.graph = scene.graph
        self.plotMapper = self.scene.plotMapper
        self.locationManager = LocationManager(self.graph)
        self.taskManager = TaskManager(self.scene)
        self.agentManager = AgentManager(robotManager, self.locationManager, self.taskManager, self.plotMapper, self.graph)
    
    def step(self):
        self.agentManager.step()

