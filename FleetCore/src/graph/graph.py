from graph.shortestPathPlanner import ShortestPathPlanner
from graph.graphUtils import GraphUtils

class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.nodeCount = 0
        self.nodeDict = {}
        self.edgeDict = {}
        self.pathPlanner = ShortestPathPlanner(self)
        self.graphUtils = GraphUtils(self)
    
    def addNode(self, node):
        self.nodes.append(node)
        self.nodeCount += 1
        self.nodeDict[node.name] = node
    
    def addEdge(self, edge):
        self.edges.append(edge)
        self.edgeDict[(edge.fromNode, edge.toNode)] = edge
        edge.fromNode.reachableNodes.append(edge.toNode)
    
    def findPath(self, pos, goal):
        start = self.graphUtils.getNearestNode(pos)
        return self.pathPlanner.getPath(start, goal)

    