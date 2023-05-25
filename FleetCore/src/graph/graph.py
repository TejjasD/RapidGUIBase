import sys
sys.dont_write_bytecode = True
sys.path.append('FleetCore/')

from FleetCore.src.graph.node import Node
from FleetCore.src.graph.edge import Edge

class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodeCount = 0
        self.nodeDict = {}
        self.edgeDict = {}
    
    def addNode(self, node):
        self.nodes.append(node)
        self.nodeCount += 1
        self.nodeDict[node.name] = node
    
    def addEdge(self, edge):
        self.edges.append(edge)
        self.edgeDict[(edge.fromNode, edge.toNode)] = edge

    