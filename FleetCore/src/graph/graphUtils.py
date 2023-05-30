
class GraphUtils:

    def __init__(self, graph):
        self.graph = graph
    
    def getNearestNode(self, pos):
        minDist = float("inf")
        nearestNode = None
        for node in self.graph.nodes:
            dist = ((node.x - pos[0])**2 + (node.y - pos[1])**2)**0.5
            if dist == 0:
                return node
            elif dist < minDist:
                minDist = dist
                nearestNode = node
        return nearestNode
    
    def getExtreamDistances(self):
        minX = float("inf")
        minY = float("inf")
        maxX = -float("inf")
        maxY = -float("inf")
        for node in self.graph.nodes:
            if node.x < minX:
                minX = node.x
            if node.x > maxX:
                maxX = node.x
            if node.y < minY:
                minY = node.y
            if node.y > maxY:
                maxY = node.y
        return [minX, maxX, minY, maxY]
            


