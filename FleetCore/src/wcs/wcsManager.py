import random

from task.task import Task

class WcsManager:

    def __init__(self, graph):
        self.graph = graph
        self.dropLocations = []
        self.findDropLocations()


    def createTask(self, agent):
        number = random.randint(0, len(self.dropLocations) - 1)
        dropLocation = self.dropLocations[number]
        return Task(agent.id, agent.localGoal, dropLocation)

    def findDropLocations(self):
        for node in self.graph.nodes:
            if node.type == "drop":
                self.dropLocations.append(node)
    


        

