import math

class Edge:

    def __init__(self, fromNode, toNode, isUnidirectional):
        self.fromNode = fromNode
        self.toNode = toNode
        self.weight = ((fromNode.x - toNode.x)**2 + (fromNode.y - toNode.y)**2)**0.5
        self.isUnidirectional = isUnidirectional
        self.width = 2
        self.calculateBoundingBox()
        self.color = (0, 0, 0)
    

    def calculateBoundingBox(self):
        directionVector = (self.toNode.x - self.fromNode.x, self.toNode.y - self.fromNode.y)
        magnitude = math.sqrt(directionVector[0] ** 2 + directionVector[1] ** 2)
        normalizedDirection = (directionVector[0] / magnitude, directionVector[1] / magnitude)
        perpendicularVector = (-normalizedDirection[1], normalizedDirection[0])
        displacementVector = (perpendicularVector[0] * (self.width / 2), perpendicularVector[1] * (self.width / 2))

        corner1 = (self.toNode.x + displacementVector[0], self.toNode.y + displacementVector[1])
        corner2 = (self.toNode.x - displacementVector[0], self.toNode.y - displacementVector[1])
        corner3 = (self.fromNode.x - displacementVector[0], self.fromNode.y - displacementVector[1])
        corner4 = (self.fromNode.x + displacementVector[0], self.fromNode.y + displacementVector[1])

        self.bounds = [corner1, corner2, corner3, corner4]
        self.legth = magnitude










