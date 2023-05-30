import json
import random

from simulation.robot import Robot
from simulation.robotManager import RobotManager

class SimulationLoader:

    def __init__(self, path):
        self.robotManager = RobotManager()
        self.path = path


    def readScenario(self):
        with open(self.path) as file:
            data = json.load(file)

        robots = data["agents"]
        for robot in robots:
            pos = [robot["pos"]["x"], robot["pos"]["y"], robot["pos"]["z"]]
            robo = Robot(robot["id"], pos, robot["battery"])
            self.robotManager.addRobot(robo)
    

    def exportScenario(self, numAgents, graph):
        agents = []
        for i in range(1, numAgents + 1):
            randNumber = random.randint(0, len(graph.nodes) - 1)
            agent = {
                "id": str(i),
                "pos": {
                    "x": graph.nodes[randNumber].x,
                    "y": graph.nodes[randNumber].y,
                    "z": 0
                },
                "battery": random.randint(20, 100)
            }
            agents.append(agent)

        data = {"agents": agents}

        with open(self.path, "w") as file:
            json.dump(data, file, indent=4)
        print("ExportedScenario")

