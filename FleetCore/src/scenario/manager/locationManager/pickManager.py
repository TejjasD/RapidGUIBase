import random

class PickManager:

    def __init__(self, graph):
        self.graph = graph
        self.pickLocations = []
        self.findPickLocations() 

    def findPickLocations(self):
        for node in self.graph.nodes:
            if node.type == "pick":
                self.pickLocations.append(node)

    def assignPick(self, agent):
       number = random.randint(0, len(self.pickLocations) - 1)
       pickLocation = self.pickLocations[number]
       agent.goal = pickLocation
       print("Pick Assigned")

    

