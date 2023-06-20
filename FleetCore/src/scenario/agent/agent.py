from scenario.agent.agentBehaviour import AgentBehaviour
from graph.graphUtils import GraphUtils

class Agent:

    def __init__(self, robot, taskManager, locationManager):
        self.locationManager = locationManager
        self.taskManager = taskManager
        self.robot = robot
        self.pos = robot.pos
        self.battery = robot.battery
        self.id = robot.id
        self.width = 10
        self.height = 15
        self.color =  (0, 0, 139)
        self.state = "IDLE"
        self.agentBehaviour = AgentBehaviour(self)
        self.goal = None
        self.path = []
        self.reservedNodesTill = 0
        self.localGoal = None
        self.speed = 0.01
        self.task = None
        self.picked = False
        self.goalReachTolerance = 0.01
        self.vector = [0, 0]

        self.calculateBoundingBox()
        
    def calculateBoundingBox(self):
        corner1 = (self.pos[0] + self.width/2, self.pos[1] - self.height/2)
        corner2 =  (self.pos[0] + self.width/2, self.pos[1] + self.height/2)
        corner3 = (self.pos[0] - self.width/2, self.pos[1] + self.height/2)
        corner4 =  (self.pos[0] - self.width/2, self.pos[1] - self.height/2)
        self.bounds = [corner1, corner2, corner3, corner4]
    
    def step(self):
        self.clearCurrentNode()
        self.agentBehaviour.step()
        self.followPath()
        self.calculateBoundingBox()
    

    def followPath(self):   
        self.computeVector()  
        self.pos[0] += self.speed * self.vector[0]
        self.pos[1] += self.speed * self.vector[1] 

    def clearCurrentNode(self):
        if len(self.path) != 0:
            if (self.localGoal == self.path[0]):
                if len(self.path) == 1:
                    if abs(self.pos[0] - self.localGoal.x) < self.goalReachTolerance and abs(self.pos[1] - self.localGoal.y) < self.goalReachTolerance:
                        self.path.pop(0)
                        self.goal = None
                else:
                    nextGoal = self.path[1]
                    distance = GraphUtils.getDistanceBetweenNodes(self.localGoal, nextGoal)
                    coveredDistance = GraphUtils.getDistanceFromPos(self.localGoal, self.pos)
                    if coveredDistance >= 0.5 * distance:
                        self.path.pop(0)
                        self.reservedNodesTill -= 1
                        self.findNextGoal() 
    

    def findNextGoal(self):
        if len(self.path) > 0:
            if self.reservedNodesTill > 0:
                self.localGoal = self.path[0]
                self.computeVector()
    

    def computeVector(self):
        if self.localGoal is not None:
            self.vector = (self.localGoal.x - self.pos[0], self.localGoal.y - self.pos[1])
            


        
        


