import json

import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/')

from FleetCore.src.graph.graph import Graph
from FleetCore.src.graph.node import Node
from FleetCore.src.graph.edge import Edge



class SceneLoader():

    def __init__(self, path):
        self.graph = Graph()
        self.readScene(path)


    def readScene(self, path):
        with open(path) as file:
            data = json.load(file)

        nodes = data["nodes"]
        edges = data["edges"]

        for node in nodes:
            node = Node(node["x"], node["y"], node["z"], node["type"])
            self.graph.addNode(node)
        
        for edge in edges:
            edge = Edge(edge["from"], edge["to", edge["weight"], edge["isBidirectional"]])
            self.graph.addEdge(edge)


