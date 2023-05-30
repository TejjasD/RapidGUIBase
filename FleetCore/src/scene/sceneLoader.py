import json

from graph.graph import Graph
from graph.node import Node
from graph.edge import Edge
from plot.plotMapper import PlotMapper



class SceneLoader():

    def __init__(self, plotMapper, path):
        self.plotMapper = plotMapper
        self.graph = Graph()
        self.readScene(path)


    def readScene(self, path):
        with open(path) as file:
            data = json.load(file)

        nodes = data["nodes"]
        edges = data["edges"]

        for node in nodes:
            node = Node(node["name"], node["pose"]["position"]["x"], node["pose"]["position"]["y"], node["pose"]["position"]["z"], node["type"])
            self.graph.addNode(node)
        
        self.plotMapper.mapPlot(self.graph)

        for edge in edges:
            edge = Edge(self.graph.nodeDict[edge["from"]], self.graph.nodeDict[edge["to"]], edge["isUniDirectional"])
            self.graph.addEdge(edge)


