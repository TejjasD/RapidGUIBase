
class Node:

    def __init__(self, name, x, y, z, type):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.type = type
        self.color = (0, 0, 0)
        self.radius = 5
        self.reachableNodes = []
        self.pos = [x, y, z]

        if self.type == "none":
            self.color = (50, 50, 100)
        elif self.type == "pick":
            self.color = (0, 100, 0)
        elif self.type == "drop":
            self.color = (0, 0, 150)
        elif self.type == "charge":
            self.color = (100, 0, 0)
        elif self.type == "wait":
            self.color = (100, 100, 0)
        elif self.type == "queue":
            self.color = (100, 0, 100)
        else:
            self.color = (50, 50, 100)

    