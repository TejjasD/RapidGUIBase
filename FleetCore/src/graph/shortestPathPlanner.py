import heapq

class ShortestPathPlanner:

    def __init__(self, graph):
        self.graph = graph
    
    def getPath(self, startNode, endNode):
        # return [startNode, endNode]
        path = self.aStar(startNode, endNode)
        return path

    def calculateHeuristic(self, startNode, endNode):
        return ((startNode.x - endNode.x)**2 + (startNode.y - endNode.y)**2)**0.5


    def aStar(self, start, end):
        openSet = [(0, start)]  # List for open set
        gScores = {start: 0}  # Dictionary for g scores
        parentMap = {start: None}  # Dictionary to store parent nodes

        while openSet:
            current = min(openSet, key=lambda node: node[0] + self.calculateHeuristic(node[1], end))

            if current[1] == end:
                return self.reconstructPath(parentMap, end)

            openSet = [node for node in openSet if node[1] != current[1]]

            for neighbor in current[1].reachableNodes:
                distance = self.calculateHeuristic(neighbor, current[1])
                newG = gScores[current[1]] + distance

                if neighbor not in gScores or newG < gScores[neighbor]:
                    gScores[neighbor] = newG
                    parentMap[neighbor] = current[1]

                    f = newG + self.calculateHeuristic(neighbor, end)
                    openSet.append((f, neighbor))

        return None  # No path found


    def reconstructPath(self, parentMap, end):
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = parentMap[current]

        return list(reversed(path))



    